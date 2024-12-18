package com.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.DevToolsException;
import org.openqa.selenium.devtools.v85.network.Network;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

import java.util.Optional;

public class BaseTest {
    protected WebDriver driver;
    protected DevTools devTools;

    @BeforeClass
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
        devTools = ((ChromeDriver) driver).getDevTools();
        devTools.createSession();
    }

    @AfterClass
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    protected void enableNetwork() {
        devTools.send(Network.enable(Optional.empty(), Optional.empty(), Optional.empty()));
    }
}
