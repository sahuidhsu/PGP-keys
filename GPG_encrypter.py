#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Author: 天神   -*-

import os

running = True
while running:
    print("-" * 50)
    print("欢迎使用天神のGPG纯文本加密/解密器!")
    print("1. 加密")
    print("2. 解密")
    print("0. 退出")
    print("-" * 50)
    choice = input("请输入你的选择: ")
    if choice == "1":
        print("你选择了加密")
        text = input("请输入明文：")
        num_of_recipients = int(input("请输入收件人数量："))
        recipients = []
        for i in range(num_of_recipients):
            recipients.append(input("请输入收件人" + str(i+1) + "的名字或秘钥ID："))
        sign = input("是否需要签名这个信息？(y/N)")
        if sign == "y":
            command = "echo '" + text + "' | gpg -se -r " + " -r ".join(recipients) + " -a"
        else:
            command = "echo '" + text + "' | gpg -e -r " + " -r ".join(recipients) + " -a"
        print("正在加密...")
        os.system(command)
        print("加密完成！")
    elif choice == "2":
        print("你选择了解密")
        cipher = ""
        stopword = ":q"
        print("请输入密文(粘贴完成后先回车，再以':q'结束)：")
        for line in iter(input, stopword):
            cipher += line + "\n"
        print("正在解密...")
        command = "echo '" + cipher + "' | gpg -d -a -q"
        print("解密结果：")
        print("-" * 50)
        os.system(command)
        print("\n" + "-" * 50)
        print("解密完成！")
    elif choice == "0":
        print("感谢你的使用")
        running = False
