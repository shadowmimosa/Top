import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(email_configure):
    ret = True
    try:
        server = smtplib.SMTP_SSL(email_configure["hostname"],
                                  email_configure["port"])
        server.login(email_configure["username"], email_configure["password"])

        msg = MIMEText(email_configure["mail_text"],
                       email_configure["subtype"],
                       email_configure["mail_encoding"])
        msg["Subject"] = Header(email_configure["mail_subject"],
                                email_configure["mail_encoding"])
        msg["from"] = email_configure["from"]
        msg["to"] = email_configure["to"]
        server.sendmail(email_configure["from"], email_configure["to"],
                        msg.as_string())
    except Exception as exc:
        print(exc)
        ret = False

    return ret


# def bulid_boby():


def main():
    msg_html = """
    <html>

    <head>
        <meta charset="UTF-8" />
        <title>⚡ iOS 集成测试报告【v4.7.1】</title>
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="mask-icon" color="#3D4B67"
            href="http://ph.thejoyrun.com/res/phabricator/e132a80f/rsrc/favicons/mask-icon.svg" />
        <link rel="apple-touch-icon" sizes="76x76"
            href="http://ph.thejoyrun.com/file/data/qzsou6kqt4v6ph72ynxe/PHID-FILE-rzzdp6uzq7j76zchx7ha/favicon" />
        <link rel="apple-touch-icon" sizes="120x120"
            href="http://ph.thejoyrun.com/file/data/rp5fezf4o6p5tzvtenyz/PHID-FILE-27nwwiqkp6uvyv7wdn35/favicon" />
        <link rel="apple-touch-icon" sizes="152x152"
            href="http://ph.thejoyrun.com/file/data/6jzhdkxpqf3k6xpwzhlz/PHID-FILE-nr6x46fmqw6djgiuogsh/favicon" />
        <link rel="icon" id="favicon"
            href="http://ph.thejoyrun.com/file/data/eo4qbjrcm75ukxbntnb4/PHID-FILE-wta37zhitbz5spxnfpwp/favicon" />
        <meta name="referrer" content="no-referrer" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/9d1148a4/core.pkg.css" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/9fcc9773/rsrc/css/application/paste/paste.css" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/2ab25dfa/rsrc/css/layout/phabricator-source-code-view.css" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/ac68149f/rsrc/css/phui/phui-comment-form.css" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/c4ac41f9/rsrc/css/phui/phui-document.css" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/dd79b5df/rsrc/css/phui/phui-document-pro.css" />
        <link rel="stylesheet" type="text/css"
            href="http://ph.thejoyrun.com/res/redgreenX/phabricator/e68cf1fa/conpherence.pkg.css" />
        <script type="text/javascript"
            src="http://ph.thejoyrun.com/res/redgreenX/phabricator/8d83d2a1/rsrc/externals/javelin/core/init.js"></script>
    </head>

    <div class="phui-document-content-view">
        <div class="phabricator-remarkup">
            <h3 class="remarkup-header"><a name="1"></a>一）测试结论</h3>

            <p><tt class="remarkup-monospaced">Joyrun v4.7.1</tt>版本 iOS 端<tt class="remarkup-monospaced">集成测试通过</tt>，现<tt
                    class="remarkup-monospaced">可进入灰度发版阶段</tt><br />
                该需求的质量风险数据如下：</p>

            <div class="remarkup-table-wrap">
                <table class="remarkup-table">
                    <tr>
                        <th>质量指标</th>
                        <th>标准要求</th>
                        <th>实际情况</th>
                        <th>验证结果</th>
                    </tr>
                    <tr>
                        <td>遗留问题（包括历史遗留问题）的风险总值</td>
                        <td>&lt;=30</td>
                        <td>7.5</td>
                        <td>通过</td>
                    </tr>
                    <tr>
                        <td>有无&gt;=4风险值的缺陷</td>
                        <td>0</td>
                        <td>0</td>
                        <td>通过</td>
                    </tr>
                    <tr>
                        <td>机型兼容</td>
                        <td>兼容 iPhone 5 - iPhone X，iOS 8.4.1 - iOS 12.1.3</td>
                        <td>
                            <div class="paste-embed">
                                <div class="paste-embed-head"><a href="/P23">P23 iOS
                                        v4.7.1 兼容机型</a></div>
                                <div class="paste-embed-body" style="max-height: 27.6em;">
                                    <div class="phabricator-source-code-container">
                                        <table class="phabricator-source-code-view remarkup-code PhabricatorMonospaced"
                                            data-sigil="phabricator-source has-symbols" data-meta="0_44">
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>1</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 5s iOS 8.4.1
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>2</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 5c iOS 9.2.1
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>3</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 5 iOS 10.0.1
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>4</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone SE iOS 10.3.3
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>5</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 6 Plus iOS 10.3.3
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>6</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 8 iOS 11.2
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>7</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone X iOS 11.2
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>8</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 7 Plus iOS 11.2.6
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>9</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 6s iOS 11.4.1
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>10</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 7 Plus iOS 12.1.4
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="phabricator-source-line">
                                                    <span>11</span></th>
                                                <td class="phabricator-source-code">
                                                    iPhone 7 iOS 12.2 </td>
                                            </tr>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td>通过</td>
                    </tr>
                    <tr></tr>
                </table>
            </div>



            <h3 class="remarkup-header"><a name="2"></a>二）需求项目信息</h3>

            <div class="remarkup-table-wrap">
                <table class="remarkup-table">
                    <tr>
                        <th>序号</th>
                        <th>需求名称</th>
                        <th>需求优先级</th>
                        <th>产品 / 需求</th>
                        <th>开发人员</th>
                        <th>测试人员</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td><a href="/T258" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_0"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T258:
                                        用户加 V 与认证</span></span></a></td>
                        <td>最高</td>
                        <td><a href="/p/xiaomi/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_43"><span class="phui-tag-core phui-tag-color-person">@xiaomi</span></a>
                        </td>
                        <td><a href="/p/JerryFans/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_42"><span class="phui-tag-core phui-tag-color-person">@JerryFans</span></a>
                        </td>
                        <td><a href="/p/shadowmimosa/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_41"><span class="phui-tag-core phui-tag-color-person">@shadowmimosa</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td><a href="/T198" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_1"><span class="phui-tag-core phui-tag-color-object">T198:
                                    跑团主页架构调整产品文档</span></a></td>
                        <td>最高</td>
                        <td><a href="/p/maochuting/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_40"><span class="phui-tag-core phui-tag-color-person">@maochuting</span></a>
                        </td>
                        <td><a href="/p/karim/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_39"><span class="phui-tag-core phui-tag-color-person">@karim</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_38"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td><a href="/T125" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_2"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T125:
                                        跑步记录-累计总消耗-数字显示问题</span></span></a></td>
                        <td>最高</td>
                        <td><a href="/p/tanyuchen/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_37"><span class="phui-tag-core phui-tag-color-person">@tanyuchen</span></a>
                        </td>
                        <td><a href="/p/JerryFans/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_36"><span class="phui-tag-core phui-tag-color-person">@JerryFans</span></a>
                        </td>
                        <td><a href="/p/shadowmimosa/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_35"><span class="phui-tag-core phui-tag-color-person">@shadowmimosa</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td><a href="/T224" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_3"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T224:
                                        App 首页添加跑者大学入口</span></span></a></td>
                        <td>高</td>
                        <td><a href="/p/tanyuchen/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_34"><span class="phui-tag-core phui-tag-color-person">@tanyuchen</span></a>
                        </td>
                        <td><a href="/p/Blade/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_33"><span class="phui-tag-core phui-tag-color-person">@Blade</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_32"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td><a href="/T252" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_4"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T252:
                                        扫一扫-跑步中-水印相机加入扫码功能</span></span></a></td>
                        <td>中</td>
                        <td><a href="/p/tanyuchen/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_31"><span class="phui-tag-core phui-tag-color-person">@tanyuchen</span></a>
                        </td>
                        <td><a href="/p/Blade/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_30"><span class="phui-tag-core phui-tag-color-person">@Blade</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_29"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>6</td>
                        <td><a href="/T351" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_5"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T351:
                                        v4.7.1话题banner应急需求</span></span></a></td>
                        <td>最高</td>
                        <td><a href="/p/xiaomi/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_28"><span class="phui-tag-core phui-tag-color-person">@xiaomi</span></a>
                        </td>
                        <td><a href="/p/Blade/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_27"><span class="phui-tag-core phui-tag-color-person">@Blade</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_26"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>7</td>
                        <td><a href="/T263" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_6"><span class="phui-tag-core phui-tag-color-object">T263:
                                    约定跑绑定微信服务号消息推送产品文档</span></a></td>
                        <td>最高</td>
                        <td><a href="/p/maochuting/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_25"><span class="phui-tag-core phui-tag-color-person">@maochuting</span></a>
                        </td>
                        <td><a href="/p/Blade/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_24"><span class="phui-tag-core phui-tag-color-person">@Blade</span></a>
                        </td>
                        <td><a href="/p/zouzhiquan/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_23"><span class="phui-tag-core phui-tag-color-person">@zouzhiquan</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>8</td>
                        <td><a href="/T276" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_7"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T276:
                                        新增GPS定位广告跑前弹窗</span></span></a></td>
                        <td>高</td>
                        <td><a href="/p/maochuting/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_22"><span class="phui-tag-core phui-tag-color-person">@maochuting</span></a>
                        </td>
                        <td><a href="/p/Blade/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_21"><span class="phui-tag-core phui-tag-color-person">@Blade</span></a>
                        </td>
                        <td><a href="/p/shadowmimosa/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_20"><span class="phui-tag-core phui-tag-color-person">@shadowmimosa</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>9</td>
                        <td><a href="/T346" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_8"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T346:
                                        跑步记录-iOS生物识别提示文案修改</span></span></a></td>
                        <td>最高</td>
                        <td><a href="/p/tanyuchen/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_19"><span class="phui-tag-core phui-tag-color-person">@tanyuchen</span></a>
                        </td>
                        <td><a href="/p/Blade/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_18"><span class="phui-tag-core phui-tag-color-person">@Blade</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_17"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>10</td>
                        <td><a href="/T352" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_9"><span class="phui-tag-core phui-tag-color-object">T352:
                                    4.7.1 版本动态图片展示规则</span></a></td>
                        <td>最高</td>
                        <td><a href="/p/wangsiwen/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_16"><span class="phui-tag-core phui-tag-color-person">@wangsiwen</span></a>
                        </td>
                        <td><a href="/p/JerryFans/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_15"><span class="phui-tag-core phui-tag-color-person">@JerryFans</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_14"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr>
                        <td>11</td>
                        <td><a href="/T336" class="phui-tag-view phui-tag-type-object " data-sigil="hovercard"
                                data-meta="0_10"><span class="phui-tag-core-closed"><span
                                        class="phui-tag-core phui-tag-color-object">T336:
                                        分享卡片-消耗热量-自定义图片对应文案颜色</span></span></a></td>
                        <td>低</td>
                        <td><a href="/p/tanyuchen/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_13"><span class="phui-tag-core phui-tag-color-person">@tanyuchen</span></a>
                        </td>
                        <td><a href="/p/JerryFans/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_12"><span class="phui-tag-core phui-tag-color-person">@JerryFans</span></a>
                        </td>
                        <td><a href="/p/ghost/" class="phui-tag-view phui-tag-type-person " data-sigil="hovercard"
                                data-meta="0_11"><span class="phui-tag-core phui-tag-color-person">@ghost</span></a>
                        </td>
                    </tr>
                    <tr></tr>
                </table>
            </div>



            <h3 class="remarkup-header"><a name="3"></a>三）主要风险及遗留问题</h3>

            <ol class="remarkup-list">
                <li class="remarkup-list-item"><a href="http://jira.thejoyrun.com/browse/JOYRUN-5650" class="remarkup-link"
                        target="_blank" rel="noreferrer">iOS 8
                        查看勋章，会闪退</a>，线上问题，跟下个版本上线；</li>
                <li class="remarkup-list-item"><a href="http://jira.thejoyrun.com/browse/JOYRUN-5653" class="remarkup-link"
                        target="_blank" rel="noreferrer">约定跑支付完成中，点击分享跑友圈时，会自动关闭弹窗导致无法分享至跑友圈</a>，其他页面的分享不受影响，下个版本修复；
                </li>
                <li class="remarkup-list-item">少量 UI 问题。</li>
            </ol>

            <p>以上问题技术与产品经理达成一致，留待后续版本修复。</p>

            <h3 class="remarkup-header"><a name="4"></a>四）基础功能检查单</h3>

            <p><a href="http://ph.thejoyrun.com/w/test/app/v4.7.1/basic_function_checklist/" class="remarkup-link"
                    target="_blank" rel="noreferrer">iOS
                    v4.7.1 基础功能检查单</a></p>
        </div>
    </div>

    </html>
    """

    with open("2_.htm",'rb') as fn:
        msg_html_v2 = fn.read()

    email_configure_qq = {
        "from": "1169546750@qq.com",
        "to": "1169546750@qq.com",
        "hostname": "smtp.qq.com",
        "port": 465,
        "username": "1169546750@qq.com",
        "password": "zbfvcfiafdgpfiej",
        "mail_subject": "for test",
        # "mail_text": "test text",
        "mail_text": msg_html_v2,
        "mail_encoding": "utf-8",
        "subtype": "html"
    }

    email_configure_ex = {
        "from": "chexuandong@thejoyrun.com",
        "to": "chexuandong@thejoyrun.com",
        "hostname": "smtp.exmail.qq.com",
        "port": 465,
        "username": "chexuandong@thejoyrun.com",
        "password": "13196195423Xx",
        "mail_subject": "for test",
        "mail_text": "test text",
        "mail_encoding": "utf-8",
        "subtype": "plain"
    }

    ret = send_mail(email_configure_qq)

    if ret:
        print("email was seeded")
    else:
        print("seeding is failed")


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
