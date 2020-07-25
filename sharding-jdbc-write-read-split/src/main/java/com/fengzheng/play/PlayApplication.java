package com.fengzheng.play;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@MapperScan(value = "com.fengzheng.play.dao.mapper")
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class})
public class PlayApplication {

	public static void main(String[] args) {
		SpringApplication.run(PlayApplication.class, args);
	}

}
