Here's a **comprehensive and realistic exercise** designed to deeply improve your **Django model management and ORM expertise**, from basics to advanced. This single exercise involves a **complex database schema**, covers all **core and advanced ORM concepts**, and will guide you to gain mastery over Django’s **Meta options**, model relationships, querying, and optimization techniques.

---

### ✅ **Exercise Title: “Enterprise Resource Management System” (ERMS)**

You will build the backend model layer of an ERMS system used by a mid-sized company. This system manages **employees, projects, departments, tasks, leave management, appraisals, assets, and payroll**.

---

## 🔧 Exercise Objectives

You will:

1. Design a complex schema with Django models.
2. Use `Meta` class extensively for constraints, ordering, verbose names, and indexes.
3. Create various types of relationships: OneToOne, ForeignKey, ManyToMany.
4. Perform basic to advanced ORM queries: filtering, annotations, subqueries, joins, aggregations, updates.
5. Seed models with `faker` (min 100+ records per model).
6. Optimize and manage models with **custom managers**, **querysets**, and **select\_related/prefetch\_related**.

---

## 🧩 Models & Relationships

### 1. `Department`

* `name`: CharField
* `location`: CharField
* Meta:

  * `unique_together` on `name` and `location`
  * verbose\_name, ordering by name

### 2. `Employee`

* `first_name`, `last_name`, `email`, `phone_number`, `hire_date`, `is_active`: Boolean
* `department`: ForeignKey → Department
* `manager`: ForeignKey → self (nullable)
* `salary`: DecimalField
* `job_title`: CharField
* `address`: TextField
* Meta:

  * `indexes` on `email`, `department`
  * `ordering` by `hire_date desc`

### 3. `Project`

* `name`, `description`, `start_date`, `end_date`
* `budget`: DecimalField
* `department`: ForeignKey → Department
* `members`: ManyToManyField → Employee through `ProjectAssignment`

### 4. `ProjectAssignment` (intermediate model)

* `employee`: FK → Employee
* `project`: FK → Project
* `assigned_date`: DateField
* `role`: CharField
* Meta:

  * Unique constraint on `employee` and `project`

### 5. `Task`

* `title`, `description`, `status`: (choice field)
* `assigned_to`: FK → Employee
* `project`: FK → Project
* `due_date`, `completed_date`: DateTimeField
* Meta:

  * Index on `due_date`
  * ordering by `due_date`

### 6. `LeaveRequest`

* `employee`: FK → Employee
* `start_date`, `end_date`, `reason`, `status`: (choice field)
* `approved_by`: FK → Employee (nullable)
* Meta:

  * `constraints` for `start_date < end_date`

### 7. `Appraisal`

* `employee`: FK → Employee
* `reviewer`: FK → Employee
* `review_date`: DateField
* `score`: IntegerField
* `comments`: TextField

### 8. `Asset`

* `name`, `serial_number`, `purchase_date`, `assigned_to`: FK → Employee (nullable)
* `status`: (choice field)
* Meta:

  * unique on `serial_number`
  * `verbose_name_plural` set

### 9. `Payroll`

* `employee`: FK → Employee
* `month`: DateField
* `base_salary`, `bonus`, `deductions`, `net_salary`: DecimalField
* Meta:

  * Unique on `employee` and `month`
  * ordering on `month desc`

---

## 🔍 ORM Query Tasks (Grouped by Difficulty)

### 📘 **Basic ORM Queries**

1. Retrieve all employees in a given department.
2. Get all tasks assigned to a specific employee.
3. List all active projects.
4. Count employees per department.

### 📗 **Intermediate ORM Queries**

5. Fetch all projects with total budget > X.
6. Get all employees with their manager's name.
7. Get a list of projects and the number of tasks in each.
8. Annotate employees with the number of leaves taken.
9. Get payrolls of a given month with net salary > base salary.

### 📙 **Advanced ORM Queries**

10. List employees with average appraisal score > 4.
11. Retrieve top 5 departments by number of active projects.
12. Get employees who have worked on more than 3 projects.
13. Prefetch tasks and project info for employees in a single query.
14. Subquery to find employees who have not taken any leave.
15. Select all projects along with their top-performing employee (based on appraisal).
16. Get a list of assets not assigned to anyone.
17. Use `F` expressions to find tasks completed before due\_date.
18. Use `Q` objects to filter employees in multiple conditions (e.g., in HR or IT and hired after 2020).
19. Chain custom queryset methods (e.g., `active().in_department('IT').manager_only()`).
20. Use `annotate()` with `Subquery` to attach latest payroll to each employee.

---

## 🧠 Meta Class Learning Goals

Use the `Meta` class to explore:

* `ordering`
* `verbose_name` / `verbose_name_plural`
* `unique_together` (or `UniqueConstraint`)
* `indexes`
* `constraints` (CheckConstraint, etc.)
* Advanced usage like `default_related_name`

---

## ⚒️ Seeding Instructions

* Use `Faker` to create random realistic data.
* Ensure foreign key integrity while generating.
* Add 100+ rows per table (especially `Employee`, `Task`, `ProjectAssignment`, `LeaveRequest`, `Appraisal`, etc.)
* Write custom data creation scripts for complex relations (like assigning employees to projects through `ProjectAssignment`).

---

## 🚀 Bonus Challenges

* Implement a custom model manager (`EmployeeManager`) to add methods like `.active()`, `.managers_only()`.
* Create a `TaskQuerySet` with methods like `.overdue()`, `.completed()`, etc.
* Add `__str__()` methods meaningfully to all models.

---

With this exercise, you’ll cover:

* Model design best practices
* Meta class usage deeply
* All relationship types
* Full range of ORM capabilities

