import random

class Monster:
	def __init__(self):
		self.level = 1
		self.atk_slope = 10
		self.atk = 120 + self.level * self.atk_slope
		self.defence_slope = 5
		self.defence = 80 + self.level * self.defence_slope
		self.health_slope = 200
		self.health = 1000 + self.level * self.health_slope
		self.speed = 100
		self.critical = 0.12
		self.critical_rate = 1.50
		self.effect = 0
		self.effect_defence = 0

	def update(self, level = 1):
		for i in range(0, level):
			self.level += 1
			self.atk += self.atk_slope
			self.defence += self.defence_slope
			self.health += self.health_slope

	def defence_atk(self, enemy_atk):
		# update the health of monster
		self.health -= enemy_atk * 300 / (self.defence + 300)
		# print
		if self.health <= 0:
			print 'Monster is died.'

	def health(self):
		return self.health

	def speed(self):
		return self.speed

	def critical_atk(self):
		x = random.random()
		if x < self.critical:
			print '*'
			return True
		else:
			return False

	def skill_1(self, enemy):
		temp_extra_atk = self.skill_2()
		if self.critical_atk():
			enemy.defence_atk(self.atk * 1.0 * self.critical_rate + temp_extra_atk)
		else:
			enemy.defence_atk(self.atk * 1.0 + temp_extra_atk)

	def skill_2(self):
		x = random.random()
		if x < 0.2:
			print '!!'
			return self.atk * 0.4
		else:
			return 0

	def skill_3(self, enemy):
		for i in range(0,6):
			temp_extra_atk = self.skill_2()
			if self.critical_atk():
				enemy.defence_atk(self.atk * 0.5 * self.critical_rate + temp_extra_atk)
			else:
				enemy.defence_atk(self.atk * 0.5 + temp_extra_atk)
			if enemy.health() < 0:
				break


a = Monster()
b = Monster()
a_mana = 1
b_mana = 1 

while True:
	a_mana += 1
	if a_mana >= 3:
		a.skill_3(b)
		a_mana -= 3
	else:
		a.skill_1(b)
	print b.health()
	if b.health() <= 0:
		break

	b_mana += 1
	if b_mana >= 3:
		b.skill_3(a)
		b_mana -= 3
	else:
		b.skill_1(a)
	print a.health()
	if a.health() <= 0:
		break
	print ''

