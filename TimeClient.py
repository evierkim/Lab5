from Time import Time
t1 = Time( 4 , 3, 29 )
t2 = Time( 7 , 11 , 13 )
t3 = Time( 14 , 18 , 56 )
t4 = Time( 17 , 41 , 59 )
print( t1 )
print( t2 )
print( t3 )
print( t4 )
print( t1.getHours() )
print( t1.getMinutes() )
print( t1.getSeconds() )
print( t2.getHours() )
print( t2.getMinutes() )
print( t2.getSeconds() )

print( t1.timeInSeconds() )
print( t4.timeInSeconds() )

t1.changeTheTime(22,10,56)
print( t1 )

print( t2.twelveHourClock() )
print( t4.twelveHourClock() )

print( t1.whatTimeIsIt() )
print( t2.whatTimeIsIt() )
print( t3.whatTimeIsIt() )
print( t4.whatTimeIsIt() )

print( t2.compareTo(t3) )
print( t4.compareTo(t3) )

print( t3.timeTill(t4) )
print( t4.timeTill(t2) )