package com.performance.tests;

import com.performance.config.Config;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.DevToolsException;
import org.openqa.selenium.devtools.v85.network.Network;
import org.openqa.selenium.devtools.v85.network.model.LoadingFailed;
import org.openqa.selenium.devtools.v85.network.model.RequestWillBeSent;
import org.openqa.selenium.devtools.v85.network.model.ResponseReceived;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.Optional;

public class PerformanceTest {
    private WebDriver driver;
    private DevTools devTools;

    @BeforeClass
    public void setUp() {
        driver = new ChromeDriver();
        devTools = ((ChromeDriver) driver).getDevTools();
        devTools.createSession();
    }

    @Test
    public void testHomePageRenderingTime() {
        measurePageRenderingTime(Config.BASE_URL);
    }

    @Test
    public void testLoginPageRenderingTime() {
        measurePageRenderingTime(Config.LOGIN_URL);
    }

    @Test
    public void testDashboardPageRenderingTime() {
        measurePageRenderingTime(Config.DASHBOARD_URL);
    }

    private void measurePageRenderingTime(String url) {
        devTools.send(Network.enable(Optional.empty(), Optional.empty(), Optional.empty()));

        devTools.addListener(Network.requestWillBeSent(), requestWillBeSent ->
                System.out.println("Request URL: " + requestWillBeSent.getRequest().getUrl()));

        devTools.addListener(Network.responseReceived(), responseReceived ->
                System.out.println("Response URL: " + responseReceived.getResponse().getUrl() +
                        " with status: " + responseReceived.getResponse().getStatus()));

        devTools.addListener(Network.loadingFailed(), loadingFailed ->
                System.out.println("Loading failed for URL: " + loadingFailed.getRequestId()));

        long startTime = System.currentTimeMillis();
        driver.get(url);
        long endTime = System.currentTimeMillis();

        System.out.println("Page rendering time for " + url + ": " + (endTime - startTime) + " ms");
    }

    @AfterClass
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
