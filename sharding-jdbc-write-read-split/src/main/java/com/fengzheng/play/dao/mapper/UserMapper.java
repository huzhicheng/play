package com.fengzheng.play.dao.mapper;

import com.fengzheng.play.dao.entity.User;

import java.util.List;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author fengzheng
 * @since 2020-07-22
 */
public interface UserMapper{ //extends BaseMapper<User> {

    Long addUser(User user);

    List<User> list();
}
