import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestNDTShipRegression(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Wajib aktif agar bisa jalan di server GitHub
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=chrome_options
        )
        self.driver.implicitly_wait(10)
        self.base_url = "https://ndt-inspection.maritime.app"

    def test_tc_r03_submit_thickness_valid(self):
        driver = self.driver
        driver.get(f"{self.base_url}/login")

        # 1. Alur Login Inspektur
        driver.find_element(By.ID, "nip").send_keys("19940823-INSP01")
        driver.find_element(By.ID, "password").send_keys("SecureSecure123")
        driver.find_element(By.ID, "btn-login").click()
        
        # 2. Masuk ke Manifes Kapal & Mulai Inspeksi Lambung
        driver.find_element(By.CLASS_NAME, "btn-mulai-inspeksi").click()
        
        # 3. Pengisian Beruntun 5 Titik Koordinat Ketebalan Pelat (UT)
        titik_koordinat_pelat = ["14.5", "14.2", "13.8", "14.0", "14.4"]
        
        for index, nilai_tebal in enumerate(titik_koordinat_pelat, start=1):
            field_input = driver.find_element(By.ID, f"koordinat-pelat-{index}")
            field_input.clear()
            field_input.send_keys(nilai_tebal)
            time.sleep(0.5)
        
        # 4. Melakukan Submit Data Inspeksi Akhir Ke Server
        driver.find_element(By.ID, "btn-submit-inspection").click()
        
        # 5. Lapisan Asersi (Assertion) Protected Zone
        status_data = driver.find_element(By.ID, "status-data-inspeksi").text
        self.assertEqual(status_data, "Tersimpan")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
