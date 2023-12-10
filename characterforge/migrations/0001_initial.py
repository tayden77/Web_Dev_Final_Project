# Generated by Django 4.2.7 on 2023-12-08 07:48

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='APIAlignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APIBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APIClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APIFeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APIProficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APIRace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APISkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APISpell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('hair_color', models.CharField(blank=True, max_length=100, null=True)),
                ('eye_color', models.CharField(blank=True, max_length=100, null=True)),
                ('skin_color', models.CharField(blank=True, max_length=100, null=True)),
                ('trait_1', models.TextField(blank=True, null=True)),
                ('trait_2', models.TextField(blank=True, null=True)),
                ('ideals', models.TextField(blank=True, null=True)),
                ('bonds', models.TextField(blank=True, null=True)),
                ('flaws', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('faction', models.CharField(blank=True, max_length=100, null=True)),
                ('backstory', models.TextField(blank=True, null=True)),
                ('alignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='characterforge.apialignment')),
                ('background', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='characterforge.apibackground')),
            ],
        ),
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolOfMagic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('equipment_type', models.CharField(choices=[('MAGIC', 'Magic Item'), ('OTHER', 'Other')], max_length=6)),
                ('applicable_classes', models.ManyToManyField(blank=True, related_name='class_equipment', to='characterforge.apiclass')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSpell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_learned', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characterforge.character')),
                ('spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characterforge.apispell')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characterforge.character')),
                ('class_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characterforge.apiclass')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='classes',
            field=models.ManyToManyField(through='characterforge.CharacterClass', to='characterforge.apiclass'),
        ),
        migrations.AddField(
            model_name='character',
            name='equipment',
            field=models.ManyToManyField(to='characterforge.equipment'),
        ),
        migrations.AddField(
            model_name='character',
            name='feats',
            field=models.ManyToManyField(to='characterforge.apifeat'),
        ),
        migrations.AddField(
            model_name='character',
            name='proficiencies',
            field=models.ManyToManyField(to='characterforge.apiproficiency'),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='characterforge.apirace'),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(to='characterforge.apiskill'),
        ),
        migrations.AddField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(through='characterforge.CharacterSpell', to='characterforge.apispell'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
