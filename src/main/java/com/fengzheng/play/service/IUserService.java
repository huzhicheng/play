package com.fengzheng.play.service;

import com.fengzheng.play.dto.UserDto;

/**
 * IUserService
 *
 * @author fengzheng
 * @date 2020/7/19
 */
public interface IUserService {

    UserDto getUserById(String userId);
}
