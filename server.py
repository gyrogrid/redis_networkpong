import time
import redis

r = redis.Redis(host = 'localhost')

r.set('ball_x', 400)
r.set('ball_y', 300)
r.set('ball_dx', 10)
r.set('ball_dy', 15)
r.set('pad1_x', 0)
r.set('pad1_y', 300)
r.set('pad2_x', 790)
r.set('pad2_y', 300)
r.set('score1', 0)
r.set('score2', 0)


def moveball():
	
	if int(r.get('ball_y')) < 0 or int(r.get('ball_y')) > 600:
		newdy = int(r.get('ball_dy')) * -1
		r.set('ball_dy', newdy)
		
	if int(r.get('ball_x')) <= 0:
		if int(r.get('pad1_y')) <= int(r.get('ball_y')) <= int(r.get('pad1_y'))+200:
			newdx = int(r.get('ball_dx')) * -1
			r.set('ball_dx',newdx)
			print(r.get('ball_dx'), newdx)
		else:
			r.incr('score2')
			r.set('ball_x', 400)
			r.set('ball_y', 300)

	if int(r.get('ball_x')) >= 790:
		if int(r.get('pad2_y')) <= int(r.get('ball_y')) <= int(r.get('pad2_y'))+200:
			newdx = int(r.get('ball_dx')) * -1
			r.set('ball_dx',newdx)
			print(r.get('ball_dx'), newdx)
		else:
			r.incr('score1')
			r.set('ball_x', 400)
			r.set('ball_y', 300)
	

	r.incrby('ball_x', int(r.get('ball_dx')))
	r.incrby('ball_y', int(r.get('ball_dy')))

	time.sleep(.05)
	print(r.get('ball_x'), r.get('ball_y'), r.get('ball_dx'), r.get('ball_dy'), r.get('pad1_x'), r.get('pad1_y'), r.get('pad2_x'), r.get('pad2_y'), r.get('score1'), r.get('score2'))



def main():
	while 1:

		moveball()

if __name__ == '__main__':
	main()