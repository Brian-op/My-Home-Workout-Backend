from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from server.models import db, Workout, WorkoutExercise, Exercise


workout_bp = Blueprint('workout_bp', __name__)

@workout_bp.route("/", methods=["GET"])
@jwt_required()
def get_workouts():
    user_id = get_jwt_identity()
    workouts = Workout.query.filter_by(user_id=user_id).all()

    workouts_data = []
    for workout in workouts:
        exercises = [
            {
                "exercise_id": we.exercise_id,
                "name": we.exercise.name,
                "description": we.exercise.description,
                "sets": we.sets,
                "reps": we.reps
            }
            for we in workout.exercises
        ]

        workouts_data.append({
            "id": workout.id,
            "title": workout.title,
            "date": workout.date.strftime("%Y-%m-%d"),
            "exercises": exercises
        })

    return jsonify(workouts_data)



@workout_bp.route("/", methods=["POST"])
@jwt_required()
def create_workout():
    user_id = get_jwt_identity()
    data = request.get_json()

    title = data.get("title")
    date_str = data.get("date")
    exercises_data = data.get("exercises", [])

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."})

    workout = Workout(title=title, date=date_obj, user_id=user_id)
    db.session.add(workout)
    db.session.commit()

    for ex in exercises_data:
        exercise_id = ex.get("exercise_id")
        sets = ex.get("sets")
        reps = ex.get("reps")


        exercise = Exercise.query.get(exercise_id)
        if not exercise:
            return jsonify({"error": f"Exercise with ID {exercise_id} not found."}), 404

        workout_exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_id=exercise_id,
            sets=sets,
            reps=reps
        )
        db.session.add(workout_exercise)

    db.session.commit()

    return jsonify({"message": "Workout created successfully!"})


@workout_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_workout(id):
    user_id = get_jwt_identity()
    workout = Workout.query.filter_by(id=id, user_id=user_id).first()

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout deleted successfully"})
