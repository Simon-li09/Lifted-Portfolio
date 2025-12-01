from django.core.management.base import BaseCommand

from pot.models import About, FAQ, Project
from pot.models import Post


class Command(BaseCommand):
    help = 'Seed the database with sample About, FAQ and Project data for development.'

    def handle(self, *args, **options):
        if not About.objects.exists():
            About.objects.create(
                name='Alex Example',
                tagline='Senior Engineer & Product Builder',
                bio='Alex is a senior full-stack developer with a passion for building delightful, accessible products. With a background in engineering and design, Alex helps teams ship beautiful web applications and scalable APIs.',
                skills='Python\nDjango\nReact\nTailwind CSS',
                github='https://github.com/example',
                linkedin='https://www.linkedin.com/in/example/',
                website='https://example.com',
            )
            self.stdout.write(self.style.SUCCESS('Created sample About entry.'))
        else:
            self.stdout.write('About entry already exists — skipping.')

        if not FAQ.objects.exists():
            faqs = [
                {'question': 'How long does a typical project take?', 'answer': 'Most projects are completed within 4-12 weeks depending on scope and complexity.'},
                {'question': 'Do you offer ongoing support?', 'answer': 'Yes — we offer retainer-based support and SLA-backed maintenance options.'},
                {'question': 'Can you help us migrate our existing app?', 'answer': 'Absolutely — we can help audit, plan, and execute migrations with minimal downtime.'},
            ]
            for f in faqs:
                FAQ.objects.create(**f)
            self.stdout.write(self.style.SUCCESS('Created sample FAQ items.'))
        else:
            self.stdout.write('FAQ items already exist — skipping.')

        if not Project.objects.exists():
            Project.objects.create(title='Portfolio Website', description='A responsive portfolio site showcasing case studies and blog posts.', link='https://example.com')
            Project.objects.create(title='E-commerce API', description='Robust, scalable API for online stores', link='https://example.com/shop')
            self.stdout.write(self.style.SUCCESS('Created sample Projects.'))
        else:
            self.stdout.write('Projects already exist — skipping.')

        if not Post.objects.exists():
            Post.objects.create(
                title='Launching Our New Portfolio',
                slug='launching-our-new-portfolio',
                excerpt='We launched a new portfolio showcasing our latest projects and case studies.',
                content='We are excited to announce the launch of our revamped portfolio. Check out the case studies and the design improvements.',
                published=True,
            )
            Post.objects.create(
                title='How We Build Fast Web Apps',
                slug='how-we-build-fast-web-apps',
                excerpt='An inside look at our development process and optimization techniques.',
                content='Performance is key to modern web applications. We focus on accessibility, lean JS, and server-side rendering where appropriate to maintain speed.',
                published=True,
            )
            self.stdout.write(self.style.SUCCESS('Created sample Posts.'))
        else:
            self.stdout.write('Posts already exist — skipping.')

        if not Post.objects.exists():
            Post.objects.create(
                title='Announcing Our New Platform',
                slug='announcing-our-new-platform',
                excerpt='We launched a new platform that redefines how teams collaborate.',
                content='We built a new platform to help teams collaborate more effectively. Key features include... (sample content).',
                published=True,
            )
            Post.objects.create(
                title='Design System Best Practices',
                slug='design-system-best-practices',
                excerpt='A short guide to crafting a design system.',
                content='Design systems help teams produce consistent user interfaces... (sample content).',
                published=True,
            )
            self.stdout.write(self.style.SUCCESS('Created sample Posts.'))
        else:
            self.stdout.write('Posts already exist — skipping.')
