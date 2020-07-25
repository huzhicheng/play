package com.fengzheng.play.service.impl;

import com.fengzheng.play.dao.entity.User;
import com.fengzheng.play.dao.mapper.UserMapper;
import com.fengzheng.play.service.IUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author fengzheng
 * @since 2020-07-22
 */
@Service
public class UserServiceImpl implements IUserService { //extends ServiceImpl<UserMapper, User>

    @Autowired
    private UserMapper userMapper;

    @Override
    public Long addUser(User user) {
        return userMapper.addUser(user);
    }

    @Override
    public List<User> list() {
        return userMapper.list();
    }
}
