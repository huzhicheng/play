package com.fengzheng.play.service;

import com.fengzheng.play.dao.entity.User;

import java.util.List;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author fengzheng
 * @since 2020-07-22
 */
public interface IUserService {//extends IService<User> {

    Long addUser(User user);

    List<User> list();
}
