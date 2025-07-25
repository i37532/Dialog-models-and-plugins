## 1.与`ROS`通信
```
pip install pyzmq
```
- `data_publisher.py`
- `ros_listener.py`



## 2.与`stm32`通信
```
pip install pyserial
```
- `get_stm32_msg.py`<br>
监听串口，一旦满足条件，则会发布到指定信息到socket本地6000端口。

## 3.功能：
1. `JustRun.py`：  <br>
接收跑路指令，并把消息发送给`ROS`，自动导航到指定地点。 <br>
1. `Water.py`： <br>
接收用户询问，返回湿度情况。
1. `get_stm32_msg.py`<br>
接收`stm`串口通信，并在后台检测湿度变化，满足条件后唤醒，并输出语音，然后发消息给`ros`。



