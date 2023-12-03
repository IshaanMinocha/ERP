# Generated by Django 4.2.6 on 2023-12-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0002_alter_infrastructurecategories_form_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '7) Department & Rooms',
                'db_table': 'department_and_rooms',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department', models.CharField(db_column='department', max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '2) Departments',
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='InstituteDepartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(db_column='department', max_length=10, null=True, on_delete=django.db.models.deletion.SET_NULL, to='infrastructure.departments')),
            ],
            options={
                'verbose_name_plural': '6) Institite & Departments',
                'db_table': 'institute_and_departments',
            },
        ),
        migrations.CreateModel(
            name='Institutes',
            fields=[
                ('institute', models.CharField(db_column='institute', max_length=8, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '1) Institutes',
                'db_table': 'institutes',
            },
        ),
        migrations.CreateModel(
            name='ItemTypes',
            fields=[
                ('item_type', models.CharField(db_column='item_type', max_length=25, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '5) Item Types',
                'db_table': 'item_types',
            },
        ),
        migrations.CreateModel(
            name='RoomCategories',
            fields=[
                ('room_category', models.CharField(db_column='room_category', max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '4) Room Categories',
                'db_table': 'room_categories',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('room_number', models.CharField(db_column='room_number', max_length=4, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '3) Rooms',
                'db_table': 'rooms',
            },
        ),
        migrations.DeleteModel(
            name='InfrastructureCategories',
        ),
        migrations.AddField(
            model_name='institutedepartments',
            name='institute',
            field=models.ForeignKey(db_column='institute', max_length=8, null=True, on_delete=django.db.models.deletion.SET_NULL, to='infrastructure.institutes'),
        ),
        migrations.AddField(
            model_name='departmentrooms',
            name='department',
            field=models.ForeignKey(db_column='department', max_length=10, null=True, on_delete=django.db.models.deletion.SET_NULL, to='infrastructure.departments'),
        ),
        migrations.AddField(
            model_name='departmentrooms',
            name='room_number',
            field=models.ForeignKey(db_column='room_number', max_length=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='infrastructure.rooms'),
        ),
    ]
