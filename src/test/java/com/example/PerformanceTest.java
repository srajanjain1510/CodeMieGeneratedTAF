package com.example;

import org.openqa.selenium.devtools.v85.network.model.Response;
import org.testng.annotations.Test;

import java.util.HashMap;
import java.util.Map;

public class PerformanceTest extends BaseTest {

    @Test
    public void testPageRenderingTime() {
        enableNetwork();

        Map<String, Long> requestIdToStartTime = new HashMap<>();
        Map<String, Long> requestIdToEndTime = new HashMap<>();

        devTools.addListener(Network.requestWillBeSent(), request -> {
            requestIdToStartTime.put(request.getRequestId().toString(), System.currentTimeMillis());
        });

        devTools.addListener(Network.responseReceived(), response -> {
            requestIdToEndTime.put(response.getRequestId().toString(), System.currentTimeMillis());
        });

        driver.get("https://example.com");

        long totalTime = requestIdToEndTime.values().stream().mapToLong(Long::longValue).sum() -
                requestIdToStartTime.values().stream().mapToLong(Long::longValue).sum();

        System.out.println("Total Page Rendering Time: " + totalTime + " ms");
    }
}
