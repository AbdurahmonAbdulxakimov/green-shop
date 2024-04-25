from django.contrib import admin
from django.utils.translation import gettext_lazy


class MyAdminSite(admin.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy("Shop site admin")

    # Text to put in each page's <h1>.
    site_header = gettext_lazy("Shop administration")

    def get_app_list(
        self,
        request,
        app_label=None,
    ):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """

        app_dict = self._build_app_dict(request, app_label)

        # Sort the apps depending on ordering number.
        # ordering = {
        #     "Users": 1,
        #     "Projects": 2,
        # }
        # app_list = sorted(app_dict.values(), key=lambda x: ordering.get(x["name"], 10))

        # Sort the apps depending reversed on INSTALLED_APPS order.
        # allauth_accounts = app_dict.pop("account", None)
        # allauth_socials = app_dict.pop("socialaccount", None)
        # authtoken = app_dict.pop("authtoken", None)

        app_list = list(app_dict.values())[::-1]

        # Sort the models alphabetically within each app.
        for app in app_list:
            app["models"].sort(key=lambda x: x["name"])

        return app_list
