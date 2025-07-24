## 1.与`ROS`通信
- `data_publisher.py`
- `ros_listener.py`
```
pip install pyzmq
```


## 2.与`stm32`通信
- `get_stm32_msg.py`
```
pip install pyserial
```

## 3.功能：
1. `JustRun.py`：  <br>
接收跑路指令，并把消息发送给`ROS`，自动导航到指定地点。 <br>
1. `Water.py`： <br>
接收`stm`串口通信，并在后台检测湿度变化，满足条件后唤醒，并输出语音，然后发消息给`ros`


