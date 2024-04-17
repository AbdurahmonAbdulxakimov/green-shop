from django.contrib import admin
from django.utils.translation import gettext_lazy


class MyAdminSite(admin.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy("Project Management site admin")

    # Text to put in each page's <h1>.
    site_header = gettext_lazy("Project Management administration")

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        # ordering = {
        #     "Users": 1,
        #     "Projects": 2,
        # }

        app_dict = self._build_app_dict(request)

        # Sort the apps depending on ordering number.
        # app_list = sorted(app_dict.values(), key=lambda x: ordering.get(x["name"], 10))

        # Sort the apps depending reversed on INSTALLED_APPS order.
        app_list = list(app_dict.values())[::-1]

        # Sort the models alphabetically within each app.
        for app in app_list:
            app["models"].sort(key=lambda x: x["name"])

        return app_list
