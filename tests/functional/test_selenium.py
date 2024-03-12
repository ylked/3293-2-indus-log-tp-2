from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class TestSeleniumFunctional:
    """Functional tests class using selenium"""

    # TODO: Implémenter la méthode test_get_research_group qui réalise les actions suivantes:
    # - Ouvrir Firefox
    # - Se rendre sur la page www.he-arc.ch
    # - Accepter les cookies (pour éviter que certains éléments de la page ne soient cachés)
    # - Cliquer sur le bouton "Ra&D"
    # - Cliquer sur le bouton "Domaines de compétences"
    # - Ouvrir la liste "Ingénierie"
    # - Cliquer sur le groupe de compétence "Analyse de données"
    # - Vérifier que la compétence "Intelligence artificielle" soit listée dans le groupe (avec un assert)
    # Les 3 premières étapes sont déjà impléments pour vous

    def test_get_research_group(self):
        """Opens the He-Arc website and prints the list of competence from the 'Analyse de données'."""

        # Loads Geckodriver
        browser = webdriver.Firefox(
            service=Service(executable_path=GeckoDriverManager().install())
        )

        # Opens HE-Arc website.
        browser.get("https://www.he-arc.ch")

        # Accept cookies
        # cookies_button = browser.find_element(By.ID, "axeptio_btn_acceptAll")
        # cookies_button.click()

        ##### YOUR CODE HERE #####

        # open Ra&D dropdown
        rad = browser.find_element(By.ID, "w-dropdown-toggle-3")
        rad.click()

        # click on "Domaines de compétences"
        # select menu
        menu = browser.find_element(
            By.ID, "pane-v-recherche-appliquee-et-developpement"
        )

        # get 2nd link of menu and click on it
        link = menu.find_elements(By.CLASS_NAME, "menu-pane__link")[1]
        link.click()

        # open drop down menu
        ing = browser.find_element(
            By.ID, "accordion-block_bfd4fb443d60a02a4b0086b5b527e66b"
        )
        ing.click()

        path = '//div[@id="accordion-pane-block_bfd4fb443d60a02a4b0086b5b527e66b"]/div/div/ul[5]/li[1]'
        browser.find_element(By.XPATH, path).click()

        path = '//div[@id="accordion-block_346013a7ba2820d27b83ed1e037e8294"]/div/h2'
        h2 = browser.find_element(By.XPATH, path)
        assert h2.text == "Intelligence artificielle"

        ##########################

        # Close Geckodriver
        browser.quit()
