# my-compute
基于django的简易计算器
版本更新：
1. computev1:纯js实现的计算器
    * 说明：纯前端js实现，通过js的eval函数进行计算，并进行算式合法校验
2. compute_ajax:ajax实现的计算器
    * 说明：实现将用户输入的算式通过AJAX到后端通过Python的eval函数进行计算，并进行算式合法校验
3. compute_history：带用户认证和计算历史的计算器
    * 说明：用户先通过登录进入计算器，登录成功会返回该用户所有的计算历史，使用session进行会话保持，用户的计算历史保存到sqlite数据库中
    * 待改进：用户当前进行计算的结果不能动态显示到计算历史区，需要手动刷新页面才可以获得最新的计算历史
