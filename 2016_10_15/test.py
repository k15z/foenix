import unittest

ready = True
if ready:
    from code import TimeInterval
else:
    from solution import TimeInterval

class TestTimeInterval(unittest.TestCase):
    def test0(self):
    	ti = TimeInterval("1 second")
    	self.assertAlmostEqual(ti.getHours(), 1.0/3600.0)
    	self.assertAlmostEqual(ti.getMinutes(), ti.getHours() * 60.0)
    	self.assertAlmostEqual(ti.getSeconds(), ti.getMinutes() * 60.0)

    def test1(self):
    	ti = TimeInterval("1 second, 1 secoNds")
    	self.assertAlmostEqual(ti.getHours(), 2.0/3600.0)
    	self.assertAlmostEqual(ti.getMinutes(), ti.getHours() * 60.0)
    	self.assertAlmostEqual(ti.getSeconds(), ti.getMinutes() * 60.0)

    def test2(self):
    	ti = TimeInterval("1 hoUr, 2 minutes, \n1 second, 1 seconds")
    	self.assertAlmostEqual(ti.getHours(), 1.0 + 2.0 / 60.0 + 2.0/3600.0)
    	self.assertAlmostEqual(ti.getMinutes(), ti.getHours() * 60.0)
    	self.assertAlmostEqual(ti.getSeconds(), ti.getMinutes() * 60.0)

    def test3(self):
        ti = TimeInterval("1 hour, \t1 second, 2 miNutes, 50 seconds")
        self.assertAlmostEqual(ti.getHours(), 1.0 + 2.0 / 60.0 + 51.0/3600.0)
        self.assertAlmostEqual(ti.getMinutes(), ti.getHours() * 60.0)
        self.assertAlmostEqual(ti.getSeconds(), ti.getMinutes() * 60.0)

    def test4(self):
        ti = TimeInterval("100 hour, \t1 second, 2 miNutes, 50 seconds")
        self.assertAlmostEqual(ti.getHours(), 100.0 + 2.0 / 60.0 + 51.0/3600.0)
        self.assertAlmostEqual(ti.getMinutes(), ti.getHours() * 60.0)
        self.assertAlmostEqual(ti.getSeconds(), ti.getMinutes() * 60.0)

if __name__ == '__main__':
    unittest.main()
