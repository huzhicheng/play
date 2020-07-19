package com.fengzheng.play.controller;

import com.fengzheng.play.service.IUserService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * TestController
 *
 * @author fengzheng
 * @date 2020/7/19
 */
@RestController
@RequestMapping(value ="test")
public class TestController {

    private IUserService userService;

    @GetMapping(value = "user1")
    public String getUser1(@RequestParam(value = "userId") String userId) {
        userService.getUserById(userId);
        return "ok";
    }


    @GetMapping(value = "user2")
    public String getUser2(@RequestParam(value = "userId") String userId) {
        userService.getUserById(userId);
        return "ok";
    }


}
