package com.fengzheng.play.controller;

import org.springframework.boot.availability.AvailabilityChangeEvent;
import org.springframework.boot.availability.ReadinessState;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.ApplicationEventPublisherAware;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * PlayController
 *
 * @author fengzheng
 * @date 2020/6/20
 */
@RestController
public class PlayController {

    private final ApplicationEventPublisher publisher;

    public PlayController(ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }

    @GetMapping(value = "play")
    public String play() throws InterruptedException{
        Thread.sleep(6000);
        return "hey, play with me!";
    }

    @GetMapping(value = "up")
    public String up(){
        AvailabilityChangeEvent.publish(publisher,this, ReadinessState.ACCEPTING_TRAFFIC);
        return "up";
    }

    @GetMapping(value = "down")
    public String down(){
        AvailabilityChangeEvent.publish(publisher,this, ReadinessState.REFUSING_TRAFFIC);
        return "down";
    }
}
