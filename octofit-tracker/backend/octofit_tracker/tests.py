from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='spiderman', email='spiderman@marvel.com')
        self.assertEqual(user.email, 'spiderman@marvel.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='spiderman', type='Jumping', duration=10)
        self.assertEqual(activity.type, 'Jumping')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Avengers', points=200)
        self.assertEqual(lb.team, 'Avengers')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Yoga', difficulty='Easy')
        self.assertEqual(workout.name, 'Yoga')
