from poium import Page, PageElement as pel, PageElements as pels


class base_widget(Page):
    # <editor-fold desc="登录">
    login_user = pel(id_="UserName", timeout=30, describe='用户名')
    login_pass = pel(id_='Password', timeout=30, describe='密码')
    login_submit = pel(tag='button', describe='登录')
    login_done_wait = pel(css='#PrisonerMoneyInChart .zr-element:nth-child(3)', timeout=60)
    # </editor-fold>

    # <editor-fold desc="外围控件">
    win_top_close = pel(css='.layui-layer-ico',timeout=1, describe='弹窗关闭按钮')
    system_logout = pel(css='.fa-sign-out', describe='【退出】注销')
    win_min_close = pel(css='.active > .fa')

    # </editor-fold>

    # <editor-fold desc="公用">
    win_error = pel(css='#Prisoner_ErrorWF div')
    btn_next = pel(link_text='下一步', describe='【下一步】')
    win_refresh = pel(css='.columns > .btn', describe='刷新')
    win_prisoner_confirm = pel(css='.confirm', describe='确定弹窗')
    dialog_h2 = pel(tag='h2', describe='【h2提示标签】')
    win_top_confirm = pel(link_text='确定')

    fun_btn_nth5 = pel(css='.btn:nth-child(5)', describe='罪犯信息导入', timeout=10)

    money_manage_in_file_upload = pel(link_text='模板文件上传', describe='【上传文件】', timeout=10)

    btn_file_upload = pel(link_text='上传文件')

    input_file_upload = pel(class_name="webuploader-element-invisible", timeout=10, describe='上传文件框')

    btn_search = pel(css='.no-margins-search')

    # </editor-fold>

    # <editor-fold desc="资金业务管理">
    money_manage_in_add = pel(class_name='btn-primary', timeout=30, describe='添加上账/下帐')

    # 资金上账
    money_manager = pel(link_text='资金业务管理')
    money_manage_in = pel(link_text='资金上账', describe='【子节点】资金上账')

    money_manage_in_add_class = pel(css='#PrisonerMoneyInWF_TopPrisonerMoneyTypeID_chosen span', timeout=30,
                                    describe='资金分类')
    money_manage_in_add_class_check = pel(css='.active-result:nth-child(4)', describe='【选择监狱】')
    money_manage_in_add_type = pel(css='#PrisonerMoneyInWF_ChildPrisonerMoneyTypeID_chosen span', timeout=30,
                                   describe='资金分类')
    money_manage_in_add_type_check = pel(css='.active-result:nth-child(2)', describe='【选择监狱】')

    money_manage_in_file_submit = pel(id_="PrisonerMoneyInForm_FileUrl_UploadFileForm_SubmitButton", describe='【开始上传】')
    money_manage_in_cont = pel(id_='PrisonerMoneyInWF_Mark', describe='资金上账备注')
    money_manage_in_close = pel(link_text='关闭', describe='上账完成关闭页面')

    money_manage_in_check = pel(css='tr:nth-child(1) .btn:nth-child(3)', describe='审核')
    money_manage_in_submit = pel(css='tr:nth-child(1) .btn:nth-child(2)', describe='提交上账')
    money_manage_in_check_cont = pel(id_='PrisonerMoneyInCF_CheckOpinion', describe='审核上账备注')
    money_manage_in_check_submit = pel(css='.btn-info:nth-child(1)', describe='提交审核')

    # 资金下帐
    money_manage_out = pel(link_text='资金下账', describe='【子节点】资金下账')
    money_manage_out_add_class = pel(css='#PrisonerMoneyOutWF_TopPrisonerMoneyTypeID_chosen span', timeout=30,
                                     describe='资金类型')
    money_manage_out_add_class_check = pel(css='.active-result:nth-child(4)', describe='【选择监狱】')
    money_manage_out_add_type = pel(css='#PrisonerMoneyOutWF_ChildPrisonerMoneyTypeID_chosen span', timeout=30,
                                    describe='资金类型')
    money_manage_out_add_type_check = pel(css='.active-result:nth-child(2)', describe='【选择监狱】')

    money_manage_out_file_check = pel(class_name="webuploader-element-invisible", describe='上传文件框')
    money_manage_out_file_submit = pel(id_="PrisonerMoneyOutForm_FileUrl_UploadFileForm_SubmitButton",
                                       describe='【开始上传】')
    money_manage_out_cont = pel(id_='PrisonerMoneyOutWF_Mark', describe='资金下帐备注')
    money_manage_out_close = pel(link_text='关闭', describe='下账完成关闭页面')

    money_manage_out_check = pel(css='tr:nth-child(1) .btn:nth-child(3)', timeout=10, describe='审核')
    money_manage_out_submit = pel(css='tr:nth-child(1) .btn:nth-child(2)', timeout=10, describe='提交下账')
    money_manage_out_check_cont = pel(id_='PrisonerMoneyOutCF_CheckOpinion', describe='审核下账备注')
    money_manage_out_check_submit = pel(css='.btn-info:nth-child(1)', describe='提交审核')
    money_manage_out_result = pel(css='tr:nth-child(1) > td:nth-child(10) > font', timeout=20)

    # 出狱结算
    money_manage_leave = pel(id_='PrisonerSettleSF_Keyword', timeout=20)
    money_manage_leave_prisoner = pel(css='.input-group-btn tbody tr:nth-child(1)')
    money_manage_leave_cont = pel(id_='PrisonerSettleWF_Mark')
    money_manage_leave_submit = pel(id_='PrisonerSettleWF_SubmitButton')

    # </editor-fold>

    # <editor-fold desc="采购业务管理">
    采购_仓库 = pel(css='#GoodsBuyInForm_GoodsWarehouseID_chosen span', timeout=30)

    采购_仓库选择 = pel(css='.active-result:nth-child(2)')

    采购_供应商 = pel(css='#GoodsBuyInForm_GoodsSupplierID_chosen span', timeout=30)

    采购_供应商选择 = pel(css='#GoodsBuyInForm_GoodsSupplierID_chosen .active-result:nth-child(2)')

    purchase_goods_upload = pel(css='.btn:nth-child(5)')
    purchase_goods_upload_select = pel(class_name='webuploader-element-invisible', describe='上传文件输入框')

    purchase_goods_upload_submit = pel(id_='GoodsBuyInImport_FileUrl_UploadFileForm_SubmitButton')

    purchase_goods_submit = pel(css='.btn-primary:nth-child(1)')

    purchase_check_pass = pel(css='tr:nth-child(1) .btn:nth-child(2)', timeout=10)

    purchase_check_pass_cont = pel(id_='GoodsBuyIn_CheckCF_CheckOpinion')

    purchase_check_pass_submit = pel(css='.btn-info:nth-child(1)')

    purchase_check_pass_submit_confirm = pel(class_name='layui-layer-btn0')
    # </editor-fold>

    # <editor-fold desc="销售业务管理">
    # 供应站销售
    sell_center_prisoner = pel(id_='GoodsOrderSaleForm_Prisoner_Keyword')
    sell_center_prisoner_select = pel(css='.table-condensed tbody tr:nth-child(1)')
    sell_center_store = pel(css='.chosen-single > span')
    sell_center_store_select = pel(css='.chosen-results li:nth-child(1)', timeout=10)
    sell_center_goods = pel(id_='GoodsOrderSaleForm_Keyword')
    sell_center_goods_select = pel(css='#GoodsOrderSaleForm_dropdown tr:nth-child(2)')
    sell_center_submit = pel(id_='GoodsOrderSaleForm_SubmitButton')
    sell_center_submit_confirm = pel(id_='Modal_SaleSettyle', timeout=10)

    sell_center_submit_result = pel(css='.layui-layer-content', timeout=30)
    sell_center_submit_result_confirm = pel(link_text='确定', timeout=480)
    # </editor-fold>

    # <editor-fold desc="基础信息管理">
    base_prisoner_status = pel(css='#PrisonerSF_Status_chosen span', timeout=20)
    base_prisoner_status_select = pel(css='.chosen-results li:nth-child(2)', timeout=10)
    base_prisoner_card_status = pel(css='#Prisoner_AccountSF_GoodsOrderStatus_chosen span')
    base_prisoner_card_status_select = pel(
        css='#Prisoner_AccountSF_GoodsOrderStatus_chosen .active-result:nth-child(2)')
    base_prisoner_minBlance = pel(id_='PrisonerSF_FromBalance')

    # base_prisoner_list = pels()

    # 添加罪犯
    base_prisoner_file_upload_submit = pel(id_='PrisonerImportForm_FileUrl_UploadFileForm_SubmitButton')
    base_prisoner_add_submit = pel(id_='PrisonerImportForm_SubmitButton')
    base_prisoner_add_submit_result = pel(class_name='layui-layer-content', timeout=3)
    base_prisoner_add_submit_result_confirm = pel(link_text='确定')

    base_prisoner_account_status = pel(css='tr:nth-child(1) > td:nth-child(14) > font:nth-child(1)', timeout=20)

    # 罪犯开户
    blance_prisoner_reg = pel(css='#BankAccountSF_Status_chosen span', timeout=20)
    blance_prisoner_reg_status = pel(css='.active-result:nth-child(2)')
    blance_prisoner_reg_name = pel(id_='BankAccountWF_AccountName', timeout=10)
    blance_prisoner_reg_name_select = pel(css='.table-condensed tbody tr:nth-child(1)')
    blance_prisoner_reg_submit = pel(id_='BankAccountWF_SubmitButton')

    # </editor-fold>

    # <editor-fold desc="罪犯转监区管理">
    prisoner_switch_area = pel(css='.btn-danger', describe='批量转监区')
    prisoner_switch_area_upload = pel(css='.btn-warning', describe='模板文件上传')

    prisoner_switch_area_upload_file = pel(id_='PrisonAreaTransferWF_FileUrl_UploadFileForm_SubmitButton')

    prisoner_switch_area_upload_list = pels(css='#PrisonerSelect_ListTable tr')
    prisoner_switch_area_cont = pel(id_='PrisonAreaTransferWF_Mark')
    prisoner_switch_area_submit_result = pel(css='#ErrorResultSpan')
    # </editor-fold>

    # <editor-fold desc="转级管理>
    prisoner_switch_level_upload_submit = pel(css='#TreatLevelTransferWF_FileUrl_UploadFileForm_SubmitButton')
    # </editor-fold>
