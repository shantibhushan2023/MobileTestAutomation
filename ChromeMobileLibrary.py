# ChromeMobileLibrary.py
# Custom Robot Framework library based on your working AppiumLibrary code

from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import os
from datetime import datetime

class ChromeMobileLibrary:
    """Custom Robot Framework library for Chrome mobile automation"""
    
    def __init__(self):
        """Initialize the library with default configuration"""
        self.driver = None
        
        # Configuration variables (matching your working setup)
        self.remote_url = "http://localhost:4723"
        self.platform_name = "Android"
        self.platform_version = "10"
        self.device_name = "32007dd24e5e16cf"
        self.automation_name = "UiAutomator2"
        self.app_package = "com.android.chrome"
        self.app_activity = "com.google.android.apps.chrome.Main"
        
        print("ChromeMobileLibrary initialized successfully")
    
    def open_chrome_application(self):
        """Open Chrome application on Android device - matches your working test"""
        print("Opening Chrome application...")
        
        try:
            # Create UiAutomator2Options (modern approach)
            options = UiAutomator2Options()
            
            # Set all the capabilities from your working config
            options.platform_name = self.platform_name
            options.platform_version = self.platform_version
            options.device_name = self.device_name
            options.automation_name = self.automation_name
            
            # App-specific settings (instead of browser)
            options.set_capability("appium:appPackage", self.app_package)
            options.set_capability("appium:appActivity", self.app_activity)
            
            # Additional helpful capabilities
            options.set_capability("appium:noReset", True)
            options.set_capability("appium:newCommandTimeout", 300)
            
            # Create WebDriver connection
            self.driver = webdriver.Remote(
                command_executor=self.remote_url,
                options=options
            )
            
            print("✅ Chrome application opened successfully")
            return self.driver
            
        except Exception as e:
            print(f"❌ Error opening Chrome application: {e}")
            raise
    
    def close_chrome_application(self):
        """Close Chrome application - matches Close Application keyword"""
        print("Closing Chrome application...")
        
        if self.driver:
            try:
                self.driver.quit()
                print("✅ Chrome application closed successfully")
            except Exception as e:
                print(f"⚠️ Error closing Chrome application: {e}")
            finally:
                self.driver = None
        else:
            print("ℹ️ No Chrome application session to close")
    
    def sleep_seconds(self, seconds):
        """Sleep for specified seconds - matches Sleep keyword"""
        seconds = float(seconds)
        print(f"Sleeping for {seconds} seconds...")
        time.sleep(seconds)
    
    def capture_page_screenshot(self, filename=None):
        """Capture page screenshot - matches Capture Page Screenshot keyword"""
        if not self.driver:
            raise Exception("No active driver session. Open Chrome application first.")
        
        try:
            # Generate filename if not provided
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
            
            # Ensure screenshots directory exists
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            
            # Full path for screenshot
            filepath = os.path.join(screenshots_dir, filename)
            
            # Take screenshot
            self.driver.save_screenshot(filepath)
            print(f"✅ Screenshot saved: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"❌ Error capturing screenshot: {e}")
            raise
    
    def open_application(self, remote_url=None, **capabilities):
        """Generic open application method with custom capabilities"""
        if remote_url:
            self.remote_url = remote_url
        
        # Update configuration with provided capabilities
        for key, value in capabilities.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        return self.open_chrome_application()
    
    def close_application(self):
        """Generic close application method - alias for close_chrome_application"""
        return self.close_chrome_application()
    
    def get_driver(self):
        """Get current WebDriver instance for advanced operations"""
        return self.driver
    
    def is_application_running(self):
        """Check if Chrome application is currently running"""
        return self.driver is not None
    
    def get_device_info(self):
        """Get device information"""
        return {
            "device_name": self.device_name,
            "platform": self.platform_name,
            "platform_version": self.platform_version,
            "automation": self.automation_name
        }