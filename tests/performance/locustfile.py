"""Locust test package"""
from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    """Test class for Locust"""

    @task(1)
    def home(self):
        """Tests the home page"""
        self.client.get("/fr/")

    @task(2)
    def ag(self):
        """Tests the AG page"""
        self.client.get("/fr/billets-offres/abonnements/ag.html")

    @task(4)
    def refund(self):
        """Tests the refund page"""
        self.client.get(
            "/fr/aide-et-contact/remboursement-indemnisation/remboursements-indemnisations.html"
        )

    @task(8)
    def lost(self):
        """Tests the lost and found page"""
        self.client.get(
            "/fr/aide-et-contact/bureau-objets-trouves/saisir-avis-perte.html"
        )

    # TODO: implémenter 3 tests de plus
    #       Chaque test doit tester une route différente
    #       Chaque test doit être executé 2 fois plus de fois que le précédent.
