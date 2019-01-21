var project_uuid = ""; //项目uuid
$(document).ready(function() {
  init_wqzr_detial();
});

function init_wqzr_detial() {
  //确认挂牌相关信息
  $.ajax({
    url: basePath + "getWqzrQrgp_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        project_uuid = resultListText[0].PROJECTID;
        $("#wqzr_bdmc").text(emptyToNull(resultListText[0].BDMC));
        $("#wqzr_bdmc1").text(emptyToNull(resultListText[0].BDMC));
        $("#wqzr_xmbh").text(emptyToNull(resultListText[0].PROJECTCODE));
        $("#wqzr_gpjg").text(emptyToNull(resultListText[0].GPJG));
        $("#wqzr_gpqsrq").text(emptyToNull(resultListText[0].GPSJ));
        $("#wqzr_gpggq").text(emptyToNull(resultListText[0].GPGGQ));
        $("#wqzr_gpqmrq").text(emptyToNull(resultListText[0].GPJSSJ));
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });

  //挂牌期满日期
  //gpqmrq();

  //资产信息
  $.ajax({
    url: basePath + "getWqzrZcxx_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        //$("#zcxx_zcbh").text(resultListText[0].ZCBH);//资产编号
        $("#zcxx_zcmc").text(emptyToNull(resultListText[0].ZCMC)); //资产名称
        $("#zcxx_zclx").text(emptyToNull(resultListText[0].ZCLX));
        if (resultListText[0].YCCLFS == "1") {
          //资产包模式
          $("#zcxx_ycclfs").text("资产包模式");
        } else if (resultListText[0].YCCLFS == "2") {
          //项目模式
          $("#zcxx_ycclfs").text("项目模式");
        } else {
          $("#zcxx_ycclfs").text(" ");
        }
        $("#zcxx_zcfzr").text(emptyToNull(resultListText[0].ZCFZR)); //资产负责人
        $("#zcxx_zcssbm").text(emptyToNull(resultListText[0].ZCSSBM)); //资产所属部门
        $("#zcxx_jyjgzclxr").text(emptyToNull(resultListText[0].JYJGZCLXR)); //交易机构资产联系人
        $("#zcxx_jyjgzclxfs").text(emptyToNull(resultListText[0].JYJGZCLXFS)); //联系电话
        $("#zcxx_jyjgbmfzr").text(emptyToNull(resultListText[0].JYJGBMFZR)); //交易机构部门负责人
        $("#zcxx_jyjgbmlxfs").text(emptyToNull(resultListText[0].JYJGBMLXFS)); //联系电话
        $("#zcxx_fax").text(emptyToNull(resultListText[0].FAX)); //传真
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });

  //标的企业基本情况
  $.ajax({
    url: basePath + "getWqzrBdqy_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        for (i = 0; i < resultListText.length; i++) {
          var content = "";
          //alert(resultListText[i].TYPE);
          if (resultListText[i].TYPE == "1") {
            //机动车
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">车型</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_cx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">车型</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_cx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">车牌号</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_cph' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">购置日期</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_gzdate' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">登记日期</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_djdate' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">使用年限(年)</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_synx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">颜色</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_ys' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">行驶公里数(公里)</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_xsgls' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">数量(台 )</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_num' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">年检至</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_njz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">权证</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_qz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">评估值（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_pgz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">确认底价（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_qrdj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">表示里程</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_bslc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">交强险到期日</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_jqxdqr' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">备胎</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_bt' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">排量</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_pl' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">变速箱类型</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_bsxlx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">车钥匙</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_cys' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">缺失配件</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_qspj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">车辆识别代码</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_clsbdm' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">附加信息</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jdc_fjxx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";

            $("#bdjk_tbody").after(content);

            $("#jdc_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#jdc_cx" + i).text(emptyToNull(resultListText[i].CX));
            $("#jdc_cph" + i).text(emptyToNull(resultListText[i].CPH));
            $("#jdc_gzdate" + i).text(emptyToNull(resultListText[i].GZRQ));
            $("#jdc_djdate" + i).text(emptyToNull(resultListText[i].DJRQ));
            $("#jdc_synx" + i).text(emptyToNull(resultListText[i].SYNX));
            $("#jdc_ys" + i).text(emptyToNull(resultListText[i].YS));
            $("#jdc_xsgls" + i).text(emptyToNull(resultListText[i].XSGLS));
            $("#jdc_num" + i).text(emptyToNull(resultListText[i].SL));
            if (resultListText[i].NJZ == "" || resultListText[i].NJZ == null) {
              $("#jdc_njz" + i).text(" ");
            } else {
              $("#jdc_njz" + i).text(resultListText[i].NJZ + " 年");
            }
            $("#jdc_qz" + i).text(emptyToNull(resultListText[i].QZ));
            $("#jdc_pgz" + i).text(emptyToNull(resultListText[i].PGZ));
            $("#jdc_qrdj" + i).text(emptyToNull(resultListText[i].QRDJ));
            $("#jdc_bslc" + i).text(emptyToNull(resultListText[i].BSLC));
            $("#jdc_jqxdqr" + i).text(emptyToNull(resultListText[i].JQXDQR));
            $("#jdc_bt" + i).text(emptyToNull(resultListText[i].BT));
            $("#jdc_pl" + i).text(emptyToNull(resultListText[i].PL));
            $("#jdc_bsxlx" + i).text(emptyToNull(resultListText[i].BSXLX));
            $("#jdc_cys" + i).text(emptyToNull(resultListText[i].CYS));
            $("#jdc_qspj" + i).text(emptyToNull(resultListText[i].QSPJ));
            $("#jdc_clsbdm" + i).text(emptyToNull(resultListText[i].CLSBDM));
            $("#jdc_fjxx" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
          } else if (resultListText[i].TYPE == "2") {
            //房屋
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TD class="xmtd1" width="15%">地址</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_dz' +
              i +
              '">&nbsp;</TD>' +
              "<TR>" +
              '<TD class="xmtd1" width="15%">房产证号</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_fczg' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">建筑面积</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_jzmj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">建筑结构</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_jzjg' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">建成时间</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_jcdate' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">使用性质</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_syxz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">土地证号</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_tdzh' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">土地面积(平方米)</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_tdmj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">土地类型</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_tdlx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">使用年限</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_synx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">租赁情况</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_zlqk' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">已用年限</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_yynx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">评估值（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_sccj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">确认底价（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_qrdj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">附加信息</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fw_fjxx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";

            $("#bdjk_tbody").after(content);

            $("#fw_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#fw_dz" + i).text(emptyToNull(resultListText[i].DZ));
            $("#fw_fczg" + i).text(emptyToNull(resultListText[i].FCZH));
            $("#fw_jzmj" + i).text(emptyToNull(resultListText[i].JZMJ));
            $("#fw_jzjg" + i).text(emptyToNull(resultListText[i].JZJG));
            $("#fw_jcdate" + i).text(emptyToNull(resultListText[i].JCSJ));
            $("#fw_syxz" + i).text(emptyToNull(resultListText[i].SYXZ));
            $("#fw_tdzh" + i).text(emptyToNull(resultListText[i].TDZH));
            $("#fw_tdmj" + i).text(emptyToNull(resultListText[i].TDMJ));
            $("#fw_tdlx" + i).text(emptyToNull(resultListText[i].TDLX));
            $("#fw_synx" + i).text(emptyToNull(resultListText[i].SYNX));
            $("#fw_zlqk" + i).text(emptyToNull(resultListText[i].ZLQK));
            $("#fw_yynx" + i).text(emptyToNull(resultListText[i].YYNX));
            $("#fw_sccj" + i).text(emptyToNull(resultListText[i].PGZ));
            $("#fw_qrdj" + i).text(emptyToNull(resultListText[i].QRDJ));
            $("#fw_fjxx" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
            if (
              resultListText[i].IMGURL != null &&
              resultListText[i].IMGURL != ""
            ) {
              readMapPhoto(
                resultListText[i].UUID,
                emptyToNull(resultListText[i].IMGURL)
              );
            }
          } else if (resultListText[i].TYPE == "3") {
            //机械设备
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TD class="xmtd1" width="15%">规格型号</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_ggxh' +
              i +
              '">&nbsp;</TD>' +
              "<TR>" +
              '<TD class="xmtd1" width="15%">计量单位</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_jldw' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">数量</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_num' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">成新率(%)</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_cxl' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">生产厂家</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_sccj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">购置日期</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_gzdate' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">评估值（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_pgz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">确认底价（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jxsb_qrdj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">附加信息</TD>' +
              '<TD class="xmtd2" colSpan="5" id="jwsb_fjxx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";
            $("#bdjk_tbody").after(content);

            $("#jxsb_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#jxsb_ggxh" + i).text(emptyToNull(resultListText[i].GEXH));
            $("#jxsb_jldw" + i).text(emptyToNull(resultListText[i].JLDW));
            $("#jxsb_num" + i).text(emptyToNull(resultListText[i].SL));
            $("#jxsb_cxl" + i).text(emptyToNull(resultListText[i].CXL));
            $("#jxsb_sccj" + i).text(emptyToNull(resultListText[i].SCCJ));
            $("#jxsb_gzdate" + i).text(emptyToNull(resultListText[i].GZRQ));
            $("#jxsb_pgz" + i).text(emptyToNull(resultListText[i].PGZ));
            $("#jxsb_qrdj" + i).text(emptyToNull(resultListText[i].QRDJ));
            $("#jwsb_fjxx" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
          } else if (resultListText[i].TYPE == "4") {
            //电子办公设备
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="bgsb_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">办公设备</TD>' +
              '<TD class="xmtd2" colSpan="5" id="bgsb_fjxx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">数量</TD>' +
              '<TD class="xmtd2" colSpan="5" id="bgsb_num' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";

            $("#bdjk_tbody").after(content);

            $("#bgsb_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#bgsb_num" + i).text(emptyToNull(resultListText[i].SL));
            $("#bgsb_fjxx" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
          } else if (resultListText[i].TYPE == "5") {
            //废旧钢材
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fjgc_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1" width="15%">废旧钢材</TD>' +
              '<TD class="xmtd2" colSpan="5" id="fjgc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";

            $("#bdjk_tbody").after(content);

            $("#fjgc_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#fjgc" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
          } else if (resultListText[i].TYPE == "6") {
            //存货
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">计量单位</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_jldw' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">规格型号</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_ggxh' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">数量</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_num' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">评估值（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_pgz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">确认底价（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_qrdj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">附加信息</TD>' +
              '<TD class="xmtd2" colSpan="5" id="ch_fjxx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";

            $("#bdjk_tbody").after(content);

            $("#ch_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#ch_ggxh" + i).text(emptyToNull(resultListText[i].GEXH));
            $("#ch_jldw" + i).text(emptyToNull(resultListText[i].JLDW));
            $("#ch_num" + i).text(emptyToNull(resultListText[i].SL));
            $("#ch_pgz" + i).text(emptyToNull(resultListText[i].PGZ));
            $("#ch_qrdj" + i).text(emptyToNull(resultListText[i].QRDJ));
            $("#ch_fjxx" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
          } else if (resultListText[i].TYPE == "7") {
            //其他
            content =
              "<TR>" +
              '<TD class="xmtd1" width="15%">标的名称</TD>' +
              '<TD class="xmtd2" colSpan="5" id="qt_bdw_bdmc' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">数量</TD>' +
              '<TD class="xmtd2" colSpan="5" id="qt_num' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">评估值（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="qt_pgz' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">确认底价（万元）</TD>' +
              '<TD class="xmtd2" colSpan="5" id="qt_qrdj' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              "<TR>" +
              '<TD class="xmtd1">附加信息</TD>' +
              '<TD class="xmtd2" colSpan="5" id="qt_fjxx' +
              i +
              '">&nbsp;</TD>' +
              "</TR>" +
              '<TR id="' +
              resultListText[i].UUID +
              '" style="display:none">' +
              "</TR>";

            $("#bdjk_tbody").after(content);

            $("#qt_bdw_bdmc" + i).text(emptyToNull(resultListText[i].BDMC));
            $("#qt_num" + i).text(emptyToNull(resultListText[i].SL));
            $("#qt_pgz" + i).text(emptyToNull(resultListText[i].PGZ));
            $("#qt_qrdj" + i).text(emptyToNull(resultListText[i].QRDJ));
            $("#qt_fjxx" + i).text(emptyToNull(resultListText[i].FJXX));
            //读图片
            readImge(resultListText[i].BDMC, resultListText[i].UUID);
          }
        }
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });

  //转让方简况
  $.ajax({
    url: basePath + "getWqzrZrf_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        $("#zrfmc_zrf").text(emptyToNull(resultListText[0].ZRFMC));
        if (resultListText[0].QYCQLSGX == "1") {
          $("#qycqlsgx_zrf" + resultListText[0].UUID).text("中央企业(机构)");
        } else if (resultListText[0].QYCQLSGX == "2") {
          $("#qycqlsgx_zrf" + resultListText[0].UUID).text("本地企业(机构)");
        } else if (resultListText[0].QYCQLSGX == "3") {
          $("#qycqlsgx_zrf" + resultListText[0].UUID).text("外地企业(机构)");
        } else {
          $("#qycqlsgx_zrf" + resultListText[0].UUID).text(" ");
        }
        var lx_zrf = "";
        if (resultListText[0].ISGZ == "1") {
          lx_zrf = "国资 ";
        } else if (resultListText[0].ISGZ == "2") {
          lx_zrf = "非国资";
        } else {
          lx_zrf = " ";
        }
        if (resultListText[0].FLDBRLX == "1") {
          lx_zrf = lx_zrf + "法人";
        } else if (resultListText[0].FLDBRLX == "2") {
          lx_zrf = lx_zrf + "自然人";
        } else {
          lx_zrf = lx_zrf + " ";
        }
        $("#lx_zrf" + resultListText[0].UUID).text(lx_zrf);
        //监管
        var gzjgjg_zrf = "";
        if (resultListText[0].GZJGLX == "1") {
          $("#gzjglx_zrf" + resultListText[0].UUID).text("央企");
          if (resultListText[0].GZJGJG == "1") {
            gzjgjg_zrf = "国务院国资委监管";
          } else if (resultListText[0].GZJGJG == "2") {
            gzjgjg_zrf = "其他中央部委监管";
          } else {
            gzjgjg_zrf = " ";
          }
        } else if (resultListText[0].GZJGLX == "2") {
          $("#gzjglx_zrf" + resultListText[0].UUID).text("非央企");
          if (resultListText[0].GZJGJG == "3") {
            gzjgjg_zrf = "省（直辖市、自治区）级国资委监管  ";
          } else if (resultListText[0].GZJGJG == "4") {
            gzjgjg_zrf = "省（直辖市、自治区）级其他部门监管  ";
          } else if (resultListText[0].GZJGJG == "5") {
            gzjgjg_zrf = "地级市（区县）国资委监管  ";
          } else if (resultListText[0].GZJGJG == "6") {
            gzjgjg_zrf = "地级市（区县）其他部门监管  ";
          } else {
            gzjgjg_zrf = " ";
          }
          gzjgjg_zrf =
            gzjgjg_zrf +
            "国资监管机构地区代码:" +
            resultListText[0].GZJGJGDQDMIII;
        }
        $("#gzjgjg_zrf" + resultListText[0].UUID).text(emptyToNull(gzjgjg_zrf));
        $("#ssjthzgbmmc_zrf" + resultListText[0].UUID).text(
          trimToNull(resultListText[0].ZGJTHQTBMMCI) +
            " " +
            trimToNull(resultListText[0].ZGJTHQTBMMCII)
        );
        $("#zgjthqtbmzzjgdm_zrf" + resultListText[0].UUID).text(
          emptyToNull(resultListText[0].ZGJTHQTBMZZJGDM)
        );
        /**省市begin**/
        getProvince("szdq_zrfi");
        getCity("szdq_zrfii", resultListText[0].SZDQI);
        $("#szdq_zrfi option[value='" + resultListText[0].SZDQI + "']").attr(
          "selected",
          true
        );
        $("#szdq_zrfii option[value='" + resultListText[0].SZDQII + "']").attr(
          "selected",
          true
        );
        /**省市end**/
        $("#zcd_zrf").text(emptyToNull(resultListText[0].ZCD));
        var zczb = "";
        if (resultListText[0].ZCZBBZ == "1") {
          zczb = "人民币";
        } else if (resultListText[0].ZCZBBZ == "2") {
          zczb = "美元";
        } else if (resultListText[0].ZCZBBZ == "3") {
          zczb = "欧元";
        } else if (resultListText[0].ZCZBBZ == "4") {
          zczb = "日元";
        } else if (resultListText[0].ZCZBBZ == "5") {
          zczb = "英镑";
        } else if (resultListText[0].ZCZBBZ == "6") {
          zczb = "港元";
        } else if (resultListText[0].ZCZBBZ == "7") {
          zczb = "新加坡币";
        } else if (resultListText[0].ZCZBBZ == "8") {
          zczb = "瑞士法郎";
        } else if (resultListText[0].ZCZBBZ == "9") {
          zczb = "韩元";
        }
        $("#zczb_zrf").text(trimToNull(resultListText[0].ZCZB) + " " + zczb);
        var gslx = " ";
        if (resultListText[0].GSLX == "1") {
          gslx = "国有企业";
        } else if (resultListText[0].GSLX == "2") {
          gslx = "集体企业";
        } else if (resultListText[0].GSLX == "3") {
          gslx = "股份合作企业";
        } else if (resultListText[0].GSLX == "4") {
          gslx = "联营企业";
        } else if (resultListText[0].GSLX == "5") {
          gslx = "有限责任公司";
        } else if (resultListText[0].GSLX == "6") {
          gslx = "股份有限公司";
        } else if (resultListText[0].GSLX == "7") {
          gslx = "个体";
        } else if (resultListText[0].GSLX == "8") {
          gslx = "其他企业";
        } else if (resultListText[0].GSLX == "9") {
          gslx = "合资经营企业";
        }
        $("#gslx_zrf").text(gslx);
        var jjlx = " ";
        if (resultListText[0].JJLX == "A05001") {
          jjlx = "国资监管机构/政府部门";
        } else if (resultListText[0].JJLX == "A05002") {
          jjlx = "国有独资公司（企业）";
        } else if (resultListText[0].JJLX == "A05003") {
          jjlx = "国有控股企业";
        } else if (resultListText[0].JJLX == "A05004") {
          jjlx = "国有事业单位，国有社团等";
        } else if (resultListText[0].JJLX == "A05005") {
          jjlx = "国有及国有控股企业";
        } else if (resultListText[0].JJLX == "A05006") {
          jjlx = "国有参股企业";
        } else if (resultListText[0].JJLX == "A05007") {
          jjlx = "非国有企业";
        } else if (resultListText[0].JJLX == "A05008") {
          jjlx = "外资企业";
        } else if (resultListText[0].JJLX == "A05009") {
          jjlx = "其他";
        }
        $("#jjlx_zrf").text(jjlx);
        $("#fddbr_zrf").text(emptyToNull(resultListText[0].FDDBR));
        /**所属行业begin**/
        getSSHY1("sshy_zrf");
        getSSHY2("sshyi_zrf", resultListText[0].SSHY);
        $("#sshy_zrf option[value='" + resultListText[0].SSHY + "']").attr(
          "selected",
          true
        );
        $("#sshyi_zrf option[value='" + resultListText[0].SSHYI + "']").attr(
          "selected",
          true
        );
        /**所属行业end**/
        var jygm = " ";
        if (resultListText[0].JYGM == "1") {
          jygm = "大";
        } else if (resultListText[0].JYGM == "2") {
          jygm = "中";
        } else if (resultListText[0].JYGM == "3") {
          jygm = "小";
        }
        $("#jygm_zrf").text(jygm);
        $("#zzjgdm_zrf").text(emptyToNull(resultListText[0].ZZJGDM));
        //$("#gszcm_zrf").text(resultListText[0].GSZCM);
        //$("#cybdqycgqbl_zrf").text(resultListText[0].CYBDQYCGQBL);
        $("#nzrcgqbl_zrf").text(emptyToNull(resultListText[0].NZRCGQBL));
        $("#zrjg_zrf").text(emptyToNull(resultListText[0].ZRJG));
        $("#pzdwmc_zrf").text(emptyToNull(resultListText[0].BZDWMC));
        $("#pzwjmc_zrf").text(emptyToNull(resultListText[0].BZWJMC));
        $("#pzrq_zrf").text(emptyToNull(resultListText[0].PZRQ));
        //$("#pzwjlxjwh_zrf").text(emptyToNull(resultListText[0].PZWJLXJWH));
        var pzwhtr = " ";
        if (resultListText[0].PZWJLXJWH == "1") {
          pzwhtr = "文件";
        } else if (resultListText[0].PZWJLXJWH == "2") {
          pzwhtr = "股东会决议";
        } else if (resultListText[0].PZWJLXJWH == "3") {
          pzwhtr = "董事会决议";
        } else if (resultListText[0].PZWJLXJWH == "4") {
          pzwhtr = "批复";
        } else if (resultListText[0].PZWJLXJWH == "5") {
          pzwhtr = "总经理办公室会议决议";
        } else if (resultListText[0].PZWJLXJWH == "6") {
          pzwhtr = "职代会决议";
        } else if (resultListText[0].PZWJLXJWH == "7") {
          pzwhtr = "其他";
        }
        $("#pzwjlxjwh_zrf").text(pzwhtr);
        $("#pzwh_zrf").text(emptyToNull(resultListText[0].PZWH));
        var nbsyqk = " ";
        if (resultListText[0].NBSYQK == "1") {
          nbsyqk = "股东会决议";
          $("#nbsyqk_zrf").text(nbsyqk);
        } else if (resultListText[0].NBSYQK == "2") {
          nbsyqk = "董事会决议";
          $("#nbsyqk_zrf").text(nbsyqk);
        } else if (resultListText[0].NBSYQK == "3") {
          nbsyqk = "批复";
          $("#nbsyqk_zrf").text(nbsyqk);
        } else if (resultListText[0].NBSYQK == "4") {
          nbsyqk = "总经理办公室会议决议";
          $("#nbsyqk_zrf").text(nbsyqk);
        } else if (resultListText[0].NBSYQK == "5") {
          nbsyqk = "职代会决议";
          $("#nbsyqk_zrf").text(nbsyqk);
        } else if (resultListText[0].NBSYQK == "6") {
          nbsyqk = "其他";
          if (
            resultListText[0].NBSYQKQT != "" &&
            resultListText[0].NBSYQKQT != null
          ) {
            nbsyqk = "其他:" + resultListText[0].NBSYQKQT;
          }
          $("#nbsyqk_zrf").text(nbsyqk);
        }
        $("#lxr_zrf").text(emptyToNull(resultListText[0].LXR));
        $("#lxdh_zrf").text(emptyToNull(resultListText[0].LXDH));
        $("#fax_zrf").text(emptyToNull(resultListText[0].FAX));
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });

  //资产评估情况
  $.ajax({
    url: basePath + "getWqzrZcpg_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        $("#wqzr_pgjg").text(emptyToNull(resultListText[0].PGJG));
        $("#wqzr_hzjg").text(emptyToNull(resultListText[0].PGHZBAJG));
        $("#wqzr_hzrq").text(emptyToNull(resultListText[0].HZBARQ));
        $("#wqzr_pgjzr").text(emptyToNull(resultListText[0].PGJZR));
        $("#wqzr_zrbddypgz").text(emptyToNull(resultListText[0].ZRBDDYPG));
        $("#wqzr_pgjzrsjjg").text(emptyToNull(resultListText[0].PGJZRSJJG));
        $("#wqzr_lssws").text(emptyToNull(resultListText[0].LSSWS));
        $("#wqzr_zmjz").text(emptyToNull(resultListText[0].ZMJZ));
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });

  //披露信息
  $.ajax({
    url: basePath + "getWqzrPlxx_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        var nbjyfs = " ";
        if (resultListText[0].NBJYFS == "1") {
          nbjyfs = "股东会决议";
        } else if (resultListText[0].NBJYFS == "2") {
          nbjyfs = "董事会决议";
          $("#wqzr_nbsyqk").text(nbjyfs);
        } else if (resultListText[0].NBJYFS == "3") {
          nbjyfs = "总经理办公会议决议";
          $("#wqzr_nbsyqk").text(nbjyfs);
        } else if (resultListText[0].NBJYFS == "4") {
          nbjyfs = "其他";
          if (
            resultListText[0].NBJYFSQT != "" &&
            resultListText[0].NBJYFSQT != null
          ) {
            nbjyfs = "其他:" + resultListText[0].NBJYFSQT;
          }
          $("#wqzr_nbsyqk").text(nbjyfs);
        }
        $("#wqzr_qtplnr").text(emptyToNull(resultListText[0].ZYXXPL));

        //交易条件与受让方资格条件
        $("#wqzr_jytj_gpjg").text(emptyToNull(resultListText[0].GPJG));
        var jkzffs = " ";
        if (resultListText[0].JKZFFS == "1") {
          jkzffs = "一次性支付";
        } else if (resultListText[0].JKZFFS == "2") {
          jkzffs = "分期支付";
        }
        $("#wqzr_jytj_jkzffs").text(jkzffs);

        var isjnbzj = " ";
        if (resultListText[0].ISJNBZJ == "0") {
          isjnbzj = "否";
        } else if (resultListText[0].ISJNBZJ == "1") {
          isjnbzj = "是";
        }
        $("#wqzr_jytj_isjnbzj").text(isjnbzj);
        $("#wqzr_jytj_jnje").text(emptyToNull(resultListText[0].BZJJE));
        if (resultListText[0].JNXS != null && resultListText[0].JNXS != "") {
          var jnxs = resultListText[0].JNXS.split("");
          var jnxs_str = " ";
          if (jnxs[0] == "1") {
            jnxs_str += "现金 ";
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
          if (jnxs[1] == "1") {
            jnxs_str += "支票 ";
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
          if (jnxs[2] == "1") {
            jnxs_str += "汇票 ";
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
          if (jnxs[3] == "1") {
            jnxs_str += "网上支付 ";
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
          if (jnxs[4] == "1") {
            jnxs_str += "本票 ";
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
          if (jnxs[5] == "1") {
            jnxs_str += "本票 ";
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
          if (jnxs[6] == "1") {
            jnxs_str += "其他: " + resultListText[0].JNXSQT;
            $("#wqzr_jytj_jnfs").text(jnxs_str);
          }
        }
        $("#wqzr_jytj_jnsj").text(
          "挂牌公告期内， " +
            trimToNull(resultListText[0].JNSJXZ) +
            " 之前交纳 "
        );

        //挂牌信息
        $("#wqzr_gp_gpggq").text(
          "自公告之日起 " + trimToNull(resultListText[0].GPGGQ) + " 个工作日"
        );
        var gpqmh = " ";
        if (resultListText[0].GPQMH == "1") {
          gpqmh = "信息发布终结。";
        } else if (resultListText[0].GPQMH == "2") {
          gpqmh = "延长信息发布。";
          var ycxxfb = "";
          if (resultListText[0].YCXXFB == "1") {
            ycxxfb =
              gpqmh +
              " 不变更挂牌条件按照 " +
              resultListText[0].YCZJ +
              " 个工作日为一个周期延长，直至征集到意向受让方。";
          } else if (resultListText[0].YCXXFB == "2") {
            ycxxfb =
              gpqmh +
              " 不变更挂牌条件按照 " +
              resultListText[0].YCZJ +
              " 个工作日为一个周期延长，最多延长  " +
              resultListText[0].YCJGZQ +
              " 个周期。";
          }
          gpqmh = ycxxfb;
        } else if (resultListText[0].GPQMH == "3") {
          gpqmh = "变更公告内容，重新挂牌。";
        }
        $("#wqzr_gp_wzjdyxsrf").text(gpqmh);
        if (resultListText[0].GPQMHYJ == "1") {
          var gpqmhyj_text = "延长信息发布。";
          if (resultListText[0].YCXXFB_2 == "1") {
            gpqmhyj_text +=
              " 不变更挂牌条件按照 " +
              resultListText[0].YCZJ_2 +
              " 个工作日为一个周期延长，直至征集到新的意向受让方。";
          } else if (resultListText[0].YCXXFB_2 == "2") {
            gpqmhyj_text +=
              " 不变更挂牌条件按照 " +
              resultListText[0].YCZJ_2 +
              " 个工作日为一个周期延长，最多延长  " +
              resultListText[0].YCJGZQ_2 +
              " 个周期。";
          }
          $("#wqzr_gp_zjdyjyxsrf").text(gpqmhyj_text);
        } else if (resultListText[0].GPQMHYJ == "2") {
          $("#wqzr_gp_zjdyjyxsrf").text("协议转让");
        } else if (resultListText[0].GPQMHYJ == "3") {
          $("#wqzr_gp_zjdyjyxsrf").text("自动终结");
        }
        var jyfs = " ";
        if (resultListText[0].JYFS == "1") {
          jyfs = "网络竞价 ";
        } else if (resultListText[0].JYFS == "2") {
          jyfs = "拍卖";
        } else if (resultListText[0].JYFS == "3") {
          jyfs = "招投标";
        } else if (resultListText[0].JYFS == "4") {
          jyfs = "其他";
          if (
            resultListText[0].JYFSQT != "" &&
            resultListText[0].JYFSQT != null
          ) {
            jyfs = "其他:" + resultListText[0].JYFSQT;
          }
        } else if (resultListText[0].JYFS == "5") {
          jyfs = "动态报价";
        }
        $("#wqzr_gp_jyfs").text(jyfs);
        $("#wqzr_gp_qzbj").text(emptyToNull(resultListText[0].QZBJZTBSSFA));
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });

  //披露信息的条件
  $.ajax({
    url: basePath + "getWqzrPlxxtj_web.idt",
    async: false,
    type: "POST",
    data: { wqzr_uuid: wqzr_uuid },
    // dataType : 'json',
    success: function(data, textStatus) {
      if (data != "" && data != null) {
        var resultListText = data;
        var wqzr_jytj_yzrxgqttj = "";
        var wqzr_jytj_srfzgtj = "";
        for (var i = 0; i < resultListText.length; i++) {
          if (resultListText[i].LX == "转让条件") {
            wqzr_jytj_yzrxgqttj =
              wqzr_jytj_yzrxgqttj +
              (parseInt(resultListText[i].XH) + 1) +
              "." +
              resultListText[i].TJNR +
              "<br>";
          } else if (resultListText[i].LX == "受让条件") {
            wqzr_jytj_srfzgtj =
              wqzr_jytj_srfzgtj +
              (parseInt(resultListText[i].XH) + 1) +
              "." +
              resultListText[i].TJNR +
              "<br>";
          }
        }
        $("#wqzr_jytj_yzrxgqttj").html(wqzr_jytj_yzrxgqttj);
        $("#wqzr_jytj_srfzgtj").html(wqzr_jytj_srfzgtj);
      }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("获取数据失败！");
    }
  });
}
function readMapPhoto(uuid, url) {
  if (url != "") {
    var fj_html = "";
    fj_html += "<TR>";
    fj_html += "<TD class='xmtd1'>地图展示：</TD>";
    fj_html += "<TD class='xmtd2' id='tpzs' colSpan='5'>";
    fj_html +=
      "<iframe width='604' height='525 'frameborder='0' scrolling='no' marginheight='0' ";
    fj_html += "marginwidth='0' src='" + url + "'></iframe>";
    fj_html += "</TD>";
    fj_html += "</TR>";
    $("#" + uuid).after(fj_html);
  }
}
//显示标的图片
function readImge(bdmc, uuid) {
  var basePath = $("#basePath").val();
  //var bdmc = $("#wqzr_bdmc").text();
  //注意路径是写死的
  var tp_path =
    "E:\\WK\\saee\\projectFile\\" + project_uuid + "\\项目自身\\" + bdmc + "";
  $.ajax({
    url: basePath + "readFileImg.idt",
    type: "POST",
    async: false,
    data: "fj_iframe_path=" + tp_path + "&math=" + Math.random(),
    // dataType : 'json',
    success: function(data, textStatus) {
      var data = decodeURIComponent(data);
      var fj_html = "";
      var datas = eval("(" + data + ")");
      if (datas.length > 0) {
        fj_html += "<TR>";
        fj_html += "<TD class='xmtd1'>图片展示：</TD>";
        fj_html += "<TD class='xmtd2' id='tpzs' colSpan='5'>";
        fj_html += "<div class='workpicall'><dl>";
        for (var i = 0; i < datas.length; i++) {
          //fj_html+="<tr><td colspan='6'><img src='"+basePath+"loadImg.idt?imgPath="+encodeURI(encodeURI(datas[i].url))+"' alt='' width='100%;' height='700'/></td><tr>";
          fj_html +=
            "<dd><img src='" +
            basePath +
            "loadImg.idt?imgPath=" +
            encodeURI(encodeURI(datas[i].url)) +
            "'/></dd>";
        }
        fj_html += "</dl></div></TD></TR>";
      }
      $("#" + uuid).after(fj_html);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("服务器请求失败！");
    }
  });
}

//挂牌期满日期
function gpqmrq() {
  var gpsj = $("#wqzr_gpqsrq").text();
  var gpggq = $("#wqzr_gpggq").text(); //披露信息里的
  var gpqmrq = "";
  if ($.trim(gpsj) != "" && $.trim(gpggq) != "") {
    //挂牌公告时间和挂牌起始时间都需要才能算出截止时间
    gpqmrq = getWorkDays(gpsj, gpggq);
    if (gpqmrq != false) {
      $("#wqzr_gpqmrq").text(gpqmrq);
    }
  }
}

/**
 * 去掉字符串前后空格，null转成''
 */
function trimToNull(str) {
  return $.trim(str);
}
/**
 * 去掉空字符串
 */
function emptyToNull(str) {
  return str == null ? " " : str;
}
	