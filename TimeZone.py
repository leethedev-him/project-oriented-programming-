""" Module for import """

gmt_offsets = {
		"london": 0,
		"paris": 1,
		"dubai": 4,
		"new york": -5
	}


def convert(ITS, origin, dest):
	try:
		hrs = ITS[0 : ITS.index(":")]
		mins = ITS[(ITS.index(':') + 1) : ITS.index(' ')]

		if not hrs.isdigit():
			raise ValueError("Hour must be a string")
		else:
			if ITS[-2:] == "am":
				hrs = int(hrs)
			elif ITS[-2:] == "pm":
				hrs = int(hrs) + 12
			else:
				raise ValueError("Enter only either am or pm at the end of your time") 
			

		hr = (hrs + (gmt_offsets[dest] - gmt_offsets[origin])) 
		am_pm = "am" if hr < 12 else "pm"
		return f"{hr % 12}:{mins} {am_pm}"
	except Exception as e:
		print(f"{e}, try again")

""" End of module """

def main():
	

	def convert(input_time, origin, dest):
		hr = (input_time + (gmt_offsets[dest] - gmt_offsets[origin])) 
		am_pm = "am" if hr < 12 else "pm"
		return hr % 12, am_pm

		
	while True:
		try: 

			t = input("Enter the time in this format `HH:MMam`, eg: '04:23 am': ").strip().lower()
			
			x = t.index(':')  
			y = t.index(" ")
			hours = t[0:x]
			mins = t[x+1 : y] 

			am_pm = t[-2:]

			if not hours.isdigit():
				raise ValueError("Hour Must Be a digit (0-9)")
				
			if not mins.isdigit():
				raise ValueError("Minute Must Be a digit (0-9)")

			if int(mins) < 0 or int(mins) > 59:
				raise ValueError("Minute Must Be Between 00 and 59")
				
			origin = input("Enter the Time Zone you want to convert from: \n1 for london, 2 for paris, 3 for dubai, 4 for new york: ").strip()
			
			if len(origin) != 1 or  int(origin) > 4 or int(origin) < 1:
				raise ValueError("Enter only values between 1 and 4")

			origin = int(origin)


			if origin == 1:
				origin = "london"
			elif origin == 2:
				origin = "paris"
			elif origin == 3:
				origin = "dubai"
			else:
				origin = "new york"
			
			print(f"{t} in {origin.title()} is ")

			dest = ["london", "paris", "dubai", "new york"]

			dest = [i for i in dest if i is not origin]


			
			if am_pm == "am":
				pass
			elif am_pm == "pm":
				hours = int(hours) + 12
			else:
				raise ValueError("Enter only either am or pm at the end of your time")

				

			results = []
			for i in dest:
				results.append((convert(int(hours), origin, i)))

			for i, result in enumerate(results):
				print(f"{result[0]}:{mins} {result[1]} in {dest[i].title()}")

			break

		except Exception as e:
			print(f"{e}, An error occured, please try again. ")

if __name__ == "__main__":
	main()