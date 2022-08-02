package com.example.app3.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestParam;
import redis.clients.jedis.Jedis;
import java.util.Set;



@Service
@PropertySource("classpath:application.properties")
public class GetService {

    @Value("${host:redis-master.kong.svc.cluster.local}")
    public String host;
    @Value("${port:6379}")
    public String port;
    public String getService() {
        Jedis jedis = new Jedis(host, Integer.parseInt(port));
        Set<String> keys = jedis.keys("*");
        String s = "Number of Redis objects: " + String.valueOf(keys.size());
        return s;
    }


}
