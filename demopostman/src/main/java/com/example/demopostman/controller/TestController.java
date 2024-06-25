package com.example.demopostman.controller;


import com.example.demopostman.entity.UserInfo;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/testapi")
public class TestController {

    @GetMapping("/getStrRes")
    public String test(){
        return "testme";
    }

    @GetMapping("/getListRes")
    public ArrayList<String> testList(){
        ArrayList arr = new ArrayList();
        arr.add("apple");
        arr.add("banana");
        return arr;
    }

    @GetMapping("/getUserInfo")
    public UserInfo getUser(){
        UserInfo user = new UserInfo(12,"测试名c",30);
        return user;
    }

    @PostMapping("/getDetailInfo")
    public Map<String,Object> getMap(@RequestParam("username") String name, @RequestParam(value = "password", required = false) String pwd){
        // 打印日志信息
        System.out.println("getMapInfo");
        System.out.printf("username:%s,password:%s", name, pwd);

        // 创建返回结果的Map
        Map<String,Object> map = new HashMap<>();

        // 判断用户名是否非空且长度大于0
        if (name != null && name.length() > 0) {
            map.put("name", name);
            map.put("pwd", (pwd != null && pwd.length() > 0) ? pwd :  "666666");

            // 创建详细信息的子Map
            Map<String,Object> m = new HashMap<>();
            m.put("id", 12);
            m.put("age", 20);
            m.put("school","测试>>学校");

            // 将详细信息子Map放入主Map中
            map.put("detailInfo", m);
        } else {
            // 如果用户名无效，返回错误码和错误信息
            map.put("code", -1);
            map.put("message","请输入用户名");
        }
        // 返回结果Map
        return map;
    }


}


