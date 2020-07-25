package com.fengzheng.play.dao.entity;

import io.swagger.annotations.ApiModel;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

import java.time.LocalDateTime;
import java.util.Date;

/**
 * <p>
 * 
 * </p>
 *
 * @author fengzheng
 * @since 2020-07-22
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@ApiModel(value="User对象", description="")
public class User {//extends Model<User> {

    private static final long serialVersionUID = 1L;

    private String id;

    private String userName;

    private Integer age;

    private String phone;

    private Date createTime;

    private Date updateTime;



}
