/*
    聊天室客户端界面
    有一个名为lia的对象在py和qml间传递数据
*/

import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 2.2

Rectangle 
{
    visible: true
    height: 500
    width : 700
    id : wind
    
    TextInput {
        id: inputer
        x: 8
        y: 338
        width: 536
        height: 110
        text: qsTr("")
        font.weight: Font.ExtraLight
        font.family: "Times New Roman"
        font.pixelSize: 18
        selectByMouse: true
        
        Rectangle {
            anchors.fill: parent
            z : -1;
            color: "#bdc2c2"
        }
        
        Button {
            id: send
            x: 444
            y: 123
            width: 84
            height: 28
            text: qsTr("发送")
            
            function onclic(){
                lia.say(inputer.text)
                inputer.text = qsTr("")
                
            }
            
            onClicked:{
                onclic()
            }
        }
        Keys.enabled: true
        Keys.onReturnPressed: {
            send.onclic()
        }
        
    }
    
    Text {
        id: msgs
        x: 8
        y: 8
        width: 536
        height: 324
        text: qsTr("")
        font.pixelSize: 18
    }
    
    Rectangle {
        id: info_area
        x: 550
        y: 8
        width: 142
        height: 289
        
        Text {
            id: name_input_asker
            x: 8
            y: 8
            width: 126
            height: 25
            text: qsTr("输入你的名称:")
            font.pixelSize: 20
        }
        
        TextInput {
            id: nameinput
            x: 8
            y: 39
            width: 102
            height: 26
            text: qsTr("匿名")
            font.family: "Tahoma"
            font.pixelSize: 16
            selectByMouse: true
            
            Rectangle {
                anchors.fill: parent
                z : -1;
                color: "#dad9ea"
            }
        }
        
        Text {
            id: sad_input_asker
            x: 8
            y: 133
            width: 126
            height: 25
            text: qsTr("服务器地址")
            font.pixelSize: 20
        }
        
        TextInput {
            id: sadinput
            x: 8
            y: 164
            width: 102
            height: 26
            text: qsTr("127.0.0.1")
            font.family: "Tahoma"
            font.pixelSize: 16
            Rectangle {
                color: "#dad9ea"
                z: -1
                anchors.fill: parent
            }
            selectByMouse: true
        }
        
        Text {
            id: sport_input_asker
            x: 8
            y: 196
            width: 126
            height: 25
            text: qsTr("服务器端口")
            font.pixelSize: 20
        }
        
        TextInput {
            id: sportinput
            x: 8
            y: 227
            width: 102
            height: 26
            text: qsTr("23333")
            font.family: "Tahoma"
            font.pixelSize: 16
            Rectangle {
                color: "#dad9ea"
                z: -1
                anchors.fill: parent
            }
            selectByMouse: true
        }

        Button {
            id: logout
            x: 29
            y: 259
            width: 84
            height: 22
            visible: false
            text: qsTr("登出")

            onClicked:
            {
                lia.logout()
                
                if(!lia.logedin())
                {
                    name_input_asker.text = "输入你的名称:"
                    ip_input_asker.visible = true
                    sad_input_asker.visible = true
                    sport_input_asker.visible = true
                    
                    nameinput.readOnly = false
                    ipinput.visible = true
                    sadinput.visible = true
                    sportinput.visible = true

                    logout.visible = false
                    login.visible = true
                }
            }


        }

        Button {
            id: login
            x: 29
            y: 259
            width: 84
            height: 22
            text: qsTr("登录")
            
            onClicked:
            {
                lia.login(nameinput.text , ipinput.text , sadinput.text ,sportinput.text)
                
                if(lia.logedin())
                {
                    name_input_asker.text = "你的名称:"
                    ip_input_asker.visible = false
                    sad_input_asker.visible = false
                    sport_input_asker.visible = false
                    
                    nameinput.readOnly = true
                    ipinput.visible = false
                    sadinput.visible = false
                    sportinput.visible = false
                    
                    login.visible = false
                    logout.visible = true
                }
            }
        }
        
        Text {
            id: ip_input_asker
            x: 8
            y: 71
            width: 126
            height: 25
            text: qsTr("你的ip:")
            font.pixelSize: 20
        }
        
        TextInput {
            id: ipinput
            x: 8
            y: 102
            width: 102
            height: 26
            text: qsTr("127.0.0.1")
            font.family: "Tahoma"
            font.pixelSize: 16
            Rectangle {
                color: "#dad9ea"
                anchors.fill: parent
                z: -1
            }
            selectByMouse: true
        }

    }
    
    
    Text {
        id: memb_lis
        x: 550
        y: 332
        width: 142
        height: 116
        text: qsTr("")
        font.pixelSize: 17
        
        Rectangle {
            id: rectangle
            color: "#c6d6e7"
            z: -1
            anchors.fill: parent
        }
    }
    

    Timer {
        id: flusher
        interval: 100
        running: true
        repeat: true
        onTriggered: {
            msgs.text = lia.messages()
            memb_lis.text = lia.members()
        }
    }
    
    Text {
        id: mem_lis_title
        x: 550
        y: 303
        width: 142
        height: 23
        text: qsTr("成员列表")
        font.pixelSize: 16
    }
    
}
