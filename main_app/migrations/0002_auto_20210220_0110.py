# Generated by Django 3.1.6 on 2021-02-20 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='conditions',
        ),
        migrations.AddField(
            model_name='plant',
            name='lighting',
            field=models.CharField(choices=[('SD', 'Shade'), ('LL', 'Low Light'), ('DS', 'Direct sun')], default='SD', max_length=20),
        ),
        migrations.AddField(
            model_name='plant',
            name='waterAmount',
            field=models.CharField(choices=[('E', 'Everyday'), ('W', 'Weekly'), ('R', 'Rarely')], default='E', max_length=20),
        ),
        migrations.CreateModel(
            name='WateringDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]