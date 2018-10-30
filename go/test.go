作者：阿里云云栖社区
链接：https://www.zhihu.com/question/37787176/answer/465424718
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

package main

import (
    "fmt"
    "math/rand"
    "sync"
    "time"
)

var (
    r = rand.New(rand.NewSource(time.Now().Unix()))

    disasterSignal = make(chan string)
    accidentSignal = make(chan string)
    diseaseSignal  = make(chan string)
)

// Element : abstract factor which life consisted by
type Element interface {
    Improve()
    Depress()
    Stable()
    Enable() bool
    BeAbleHandle(event string) bool
}

type Activity interface {
    IsSuitable(life *Life) bool
    Do(life *Life)
    Interrupted()
}

type Life struct {
    Sex string
    Age time.Duration

    Health       Element
    Knowledge    Element
    Ability      Element
    RelationShip Element
    Wealth       Element
    OtherElement Element

    Work        Activity
    Study       Activity
    Exercise    Activity
    Entertain   Activity
    Rest        Activity
    OtherActive Activity

    isDoings []Activity

    vitalitySignal chan struct{}
    NaturalDeath   chan struct{}
}

func (f *Life) Join(oppositeSex *Life, love, family Element) (*Life, error) {
    if !love.Enable() || !family.Enable() || f.Sex == oppositeSex.Sex {
        return nil, fmt.Errorf("Sorry, no boby should be borned!")
    }

    boby := &Life{
        Sex:            []string{"male", "female"}[r.Intn(2)],
        Age:            0,
        isDoings:       []Activity{},
        NaturalDeath:   make(chan struct{}),
        vitalitySignal: make(chan struct{}),
    }

    return boby, nil
}

func (f *Life) Run() {
    go ExternalEndanger(f)
    // time elapses day by day
    for {
        startTime := time.Now().UTC()
        wg := &sync.WaitGroup{}

        for _, active := range []Activity{f.Study, f.Work, f.Entertain, f.Exercise, f.Rest, f.OtherActive} {
            if f.SuitableFor(active) {
                wg.Add(1)
                go func(activity Activity) {
                    defer wg.Wait()
                    activity.Do(f)
                }(active)
            }
        }

        select {
        case <-f.NaturalDeath:
            f.Close()
            fmt.Println("Life is short, make it colourful and cherish the love around all!")
            return
        case <-f.vitalitySignal:
            fmt.Println("记得买保险!")
            return
        case <-time.After(24*time.Hour - time.Now().UTC().Sub(startTime)):
            fmt.Println("One day went by...")
        }
        //wg.Wait()
        f.Age += 24 * time.Hour
    }

    fmt.Println("Goodbye, life!")
}

func (f *Life) Somehow() {
    // happened something to effect one to reach some life stage
}

func (f *Life) SuitableFor(active Activity) bool {
    return active.IsSuitable(f)
}

func (f *Life) Survive(event string) bool {
    for _, e := range []Element{f.Health, f.Knowledge, f.Ability, f.RelationShip, f.Wealth, f.OtherElement} {
        if !e.BeAbleHandle(event) {
            return false
        }
    }

    return true
}

func (f *Life) Close() {
    for _, doing := range f.isDoings {
        doing.Interrupted()
    }

    close(f.vitalitySignal)
}

var female = LifeFromSomeWhere("female")
var male = LifeFromSomeWhere("male")

func ExternalEndanger(f *Life) {
    for {
        event := ""
        select {
        case event = <-diseaseSignal:
        case event = <-disasterSignal:
        case event = <-accidentSignal:
        }

        if !f.Survive(event) {
            f.Close()
            return
        }
    }
}

func LifeFromSomeWhere(sex string) *Life {
    life := &Life{Sex: sex}
    life.Somehow()

    return life
}

func main() {
    // I don't know the question of "鸡生蛋 or 蛋生鸡"...
    newLife, err := female.Join(male, ElementImp{Type: "love"}, ElementImp{Type: "family"})
    if err == nil {
        newLife.Run()
    }
}