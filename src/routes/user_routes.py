from fastapi import APIRouter, Path, HTTPException
from models.date_model import Date
from pymongo.errors import ServerSelectionTimeoutError
from config.db import collection
from typing import Annotated
from datetime import datetime
import logging

user = APIRouter()


@user.get("/hello/{username}")
async def greet_user(username: str):
    """
    This method greets the username and retrieves the information
    about his/her birthday.
    :param username: Username to find on database to greet.
    :return: Days left to birthday.
    """
    try:
        user_data = collection.find_one({"username": username})
        if not user_data:
            # 404 or 204
            raise HTTPException(status_code=404, detail="User not exists")

        raw_birth_date = user_data.get('dateOfBirth')
        today = datetime.today()
        birth_date = datetime.strptime(raw_birth_date, '%Y-%m-%d')
        next_birth_date = birth_date.replace(year=datetime.now().year)
        if today < next_birth_date:
            delta = next_birth_date - today
            return {
                "message": f"Hello, {user_data.get('username')}! "
                           f"{delta.days} days left for your birthday"
            }
        elif today.date() == next_birth_date.date():
            return {"message": f"Hello, {user_data.get('username')}! "
                               f"Happy birthday!"}
        elif today > next_birth_date:
            next_birth_date = birth_date.replace(year=datetime.now().year + 1)
            delta = next_birth_date - today
            return {"message": f"You have already passed "
                               f"your birthday this year. "
                               f"For the next one there are: "
                               f"{delta.days} days left."}
    except ServerSelectionTimeoutError:
        logging.error("Error connecting to database")
        raise HTTPException(status_code=500, detail="User already exists")
    except HTTPException as exc:
        logging.error(f"HTTP exception raised: {exc.status_code}")
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    except Exception as ex:
        logging.error("Generic exception: ", ex)


@user.put("/hello/{username}", status_code=204)
async def create_user(username: Annotated[str,
Path(regex="^[a-zA-Z]+$")], date_of_birth: Date):
    """
    Method that inserts user in database if it passes the required validation
    :param username: Name of user, only alpha
    :param date_of_birth: Date in format %Y %m %d
    :return:
    """
    user_exists = collection.find_one({"username": username})
    if not user_exists:
        user_data = {"username": username, "dateOfBirth":
            date_of_birth.dateOfBirth.isoformat()}
        try:
            collection.insert_one(dict(user_data))
            return
        except Exception as e:
            logging.error("Error inserting USER: ", e)

    raise HTTPException(status_code=409, detail="User already exists")


@user.get("/health")
async def read_main():
    return {"status": "OK"}
