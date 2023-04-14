import time
from appium import webdriver

class Test_E:

    def setup_class(self):
        desired_caps= {
               "platformName": "Android",
               "platformVersion": "12.0.0",
               "appium:deviceName": "88Y4C19909000060",
               "appPackage": "cn.picclife.MobileAgent.dev",
               "appActivity": "cn.picclife.MobileAgent.HomeActivity",
               "unicodeKeyboard": True,
               "udid": "88Y4C19909000060",
               "deviceReadyTimeout": 20000,
               "noReset": True
               }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)

    def  test_page_1_toubaorenxinxiluru(self):
         #点击投保
         self.driver.find_element("xpath","//android.widget.TextView[@text='投保']").click()
         time.sleep(5)
         #利用坐标点击新增按钮，后续改成相对坐标
         self.driver.tap([(538,1321)])
         time.sleep(2)
         #查找产品
         self.driver.find_element("xpath","//android.widget.TextView[@text='卓越鑫生即期养老年金保险']").click()
         #点击下一步
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='同意']").click()
         time.sleep(3)
         #上传证件影像
         self.driver.find_element("xpath","//android.widget.TextView[@text='立即扫描']").click()
         time.sleep(3)
         #点击右上角按钮
         self.driver.tap([(997,127)])
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='(测试!)手动录入']").click()
         time.sleep(2)
         #再次点击右上角按钮
         self.driver.tap([(997,127)])
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='(测试!)打开相册入口']").click()
         time.sleep(3)
         #上传身份证影像信息面
         self.driver.tap([(523,686)])
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='从相册选择']").click()
         time.sleep(3)
         self.driver.tap([(125,388)])
         time.sleep(3)
         self.driver.tap([(961,169)])
         time.sleep(10)
         #上传身份证影像国徽面
         self.driver.tap([(543,1226)])
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='从相册选择']").click()
         time.sleep(3)
         self.driver.tap([(125,388)])
         time.sleep(3)
         self.driver.tap([(961,169)])
         time.sleep(10)
         #点击下一步
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(3)
         #投保人证件信息
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入姓名']")
         ele.click
         ele.send_keys("秦烈")
         time.sleep(2)
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请再次输入姓名']")
         ele.click()
         ele.send_keys("秦烈")
         time.sleep(2)
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入证件号码']")
         ele.click()
         ele.send_keys("110101195803078478")
         time.sleep(2)
         #选择生效日期
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择证件有效起期']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         #选择失效日期
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择证件有效止期']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='保存并返回']").click()
         time.sleep(3)
         #选择婚姻状态
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(3)
         #输入平均年收入
         ele = self.driver.find_element("xpath","	//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("11")
         #输入家庭年收入
         ele = self.driver.find_element("xpath","	//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("11")
         time.sleep(3)
         #向上滑动屏幕
         self.driver.swipe(start_x=0,start_y=1957,end_x=0,end_y=280,duration=3000)
         time.sleep(3)
         #选择职业
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(5)
         self.driver.tap([(153,398)])
         time.sleep(2)
         self.driver.tap([(554,385)])
         time.sleep(2)
         self.driver.tap([(911,398)])
         time.sleep(8)
         #工作单位输入
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("北京市游戏公会")
         time.sleep(3)
         #输入联系信息
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(3)
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入乡（镇）,街道']")
         ele.click()
         ele.send_keys("测试达到成都出版设集团")
         time.sleep(2)
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入小区，精确到单元/门牌号']")
         ele.click()
         ele.send_keys("测试小区21栋201")
         time.sleep(3)
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("111111")
         time.sleep(5)
         #点击保存按钮
         self.driver.find_element("xpath","//android.widget.TextView[@text='保存']").click()
         time.sleep(3)
         #输入手机号
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("18395587027")
         time.sleep(2)
         #输入邮箱信息
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='用于接收电子保单']")
         ele.click()
         ele.send_keys("18395587027@qq.com")
         time.sleep(2)
         #输入合同类型
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(3)
         #向上滑动页面
         self.driver.swipe(start_x=0,start_y=1957,end_x=0,end_y=1200,duration=3000)
         time.sleep(3)
         #居民身份
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         #点击下一步
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(10)
         #点击下一步
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(10)

    def test_page_2_jisuanbaofei(self):
         #计算保费页面
         self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[3]").click()
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView[3]").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.TextView[3]").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         ele = self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
         ele.click()
         time.sleep(1)
         ele.send_keys("200000")
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(4)

    def test_page_3_shouyirenixnxi(self):
         #受益人页面
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(4)
         self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[5]").click()
         time.sleep(3)
         ele = self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[1]")
         ele.click()
         time.sleep(2)
         ele.send_keys("180")
         time.sleep(1)
         ele = self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[2]")
         ele.click()
         ele.send_keys("80")
         time.sleep(1)
         ele = self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.EditText")
         ele.click()
         ele.send_keys("0")
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(4)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(4)

    def test_page_4_zhanghuxinxi(self):
         #账户信息
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("6029699876543220")
         time.sleep(3)
         self.driver.find_element("xpath","//android.widget.TextView[@text='请选择']").click()
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(2)
         ele = self.driver.find_element("xpath","//android.widget.EditText[@text='请输入']")
         ele.click()
         ele.send_keys("工资收入")
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(5)

    def test_page_5_querenqianming(self):
         #附件管理
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(15)
         #点击确定按钮
         self.driver.find_element("xpath","//android.widget.TextView[@text='确定']").click()
         time.sleep(3)
         #点击下一步
         self.driver.find_element("xpath","//android.widget.TextView[@text='下一步']").click()
         time.sleep(2)
         #点击双录提示按钮
         self.driver.find_element("xpath","//android.widget.TextView[@text='否']").click()
         time.sleep(3)
         #投被保人声明与授权
         self.driver.find_element("xpath","//android.widget.TextView[@text='阅读']").click()
         time.sleep(2)
         for _ in range(0,2):
             self.driver.swipe(start_x=616,start_y=1988,end_x=616,end_y=467,duration=3000)
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='已阅悉']").click()
         time.sleep(2)
         #自动转账授权书
         self.driver.find_element("xpath","//android.widget.TextView[@text='阅读']").click()
         time.sleep(2)
         for _ in range(0,2):
             self.driver.swipe(start_x=616,start_y=1988,end_x=616,end_y=467,duration=3000)
         time.sleep(2)
         self.driver.find_element("xpath","//android.widget.TextView[@text='已阅悉']").click()
         time.sleep(2)
         #人身保险投保提示书
         self.driver.find_element("xpath","//android.widget.TextView[@text='未签名']").click()
         time.sleep(2)
         for _ in range(0,6):
             self.driver.swipe(start_x=527,start_y=2000,end_x=527,end_y=222,duration=3000)
         time.sleep(10)