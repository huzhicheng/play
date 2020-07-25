package com.fengzheng.play.controller;


import com.fengzheng.play.dao.entity.User;
import com.fengzheng.play.dto.UserDto;
import com.fengzheng.play.service.IUserService;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * <p>
 * 前端控制器
 * </p>
 *
 * @author fengzheng
 * @since 2020-07-22
 */
@RestController
@RequestMapping("user")
public class UserController {

    @Autowired
    private IUserService userService;

    @GetMapping(value = "list")
    public Object list() {
        List<User> users = userService.list();
        return users;
    }

    @PostMapping(value = "add")
    public Object add(@RequestBody UserDto userDto) {
        User user = new User();
        BeanUtils.copyProperties(userDto, user);
        return userService.addUser(user);
    }
}
