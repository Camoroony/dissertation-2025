import csv
import io

def export_workout_plan_csv(workout_plan):
    max_sets = 0

    for session in workout_plan["workout_sessions"]:
        for exercise in session["exercises"]:
            if exercise["sets"] > max_sets:
                max_sets = exercise["sets"]

    header = [
        workout_plan["plan_name"],
        "Session Name",
        "Day of Week",
        "Exercise Name",
        "Number of Sets",
        "Rep goal",
        "Reps in Reserve (RIR) per set"
    ]

    for i in range(1, max_sets + 1):
        header.append(f"Set {i} Weight (kg)")
        header.append(f"Set {i} Reps")

    header.append("Notes")


    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(header)

    for session in workout_plan["workout_sessions"]:
        for exercise in session["exercises"]:
            row = [
                "",
                session["session_name"],
                session["day_of_week"],
                exercise["exercise_name"],
                exercise["sets"],
                exercise["reps"],
                exercise["reps_in_reserve"]
                    ]

            for i in range(1, max_sets + 1):
                if i <= exercise["sets"]:
                    row.extend(["", ""]) 
                else:
                    row.extend(["N/A", "N/A"])  

            row.append("")
            writer.writerow(row)

    return csv_buffer


