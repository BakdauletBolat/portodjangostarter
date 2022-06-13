import os
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = "Starts a container the porto way"

    def handle(self, *args, **options):
        app_name = options.pop("name",None)

        target = options.pop("directory")
        options["template"] = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_app_template"
        )
        super().handle("app", app_name, target, **options)
        print(f"Creating {app_name}")
        self.stdout.write(self.style.SUCCESS(f'- Successfully created porto container - {app_name} 🚢'))