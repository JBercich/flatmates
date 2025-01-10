#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pydantic
import typing
import enum
import datetime

from pydantic import BaseModel, PositiveInt
from typing import Literal, Optional
from datetime import date, datetime

AccomodationType = Literal[
    "granny-flats",
    "share-houses",
    "student-accommodation",
    "studios",
    "whole-properties",
    "homestays",
    "1-beds",
    "rooms",
]
LengthOfStay = Literal[
    "1-week",
    "2-weeks",
    "4-weeks",
    "6-weeks",
    "2-months",
    "3-months",
    "4-months",
    "6-months",
    "9-months",
    "1-year",
]
RoomShare = Literal["shared-room", "private-room"]
Accepting = Literal["males", "females", "couples"]
Furnished = Literal["furnished", "unfurnished"]
Bathrooms = Literal["ensuite-or-own", "ensuite"]
Bedroom = Literal["1-rooms", "2-rooms", "3-rooms", "4-rooms"]
Parking = Literal["no-parking", "off-street-parking", "on-street-parking"]


class Filter(pydantic.BaseModel):
    accomodation_location: str
    accomodation_type: AccomodationType = "rooms"
    minimum_amount: PositiveInt | None = None
    maximum_amount: PositiveInt | None = None
    length_of_stay: LengthOfStay | None = None
    available_from: date | None = None
    room_type: RoomShare | None = None
    accepting: Accepting | None = None
    furnished: Furnished | None = None
    bathrooms: Bathrooms | None = None
    bedroom: Bedroom | None = None
    parking: Parking | None = None
    includes_bills: bool = False
    female_housing: bool = False
    accepts_backpackers: bool = False
    accepts_children: bool = False
    accepts_lgbt: bool = False
    acceots_over_40: bool = False
    accepts_pets: bool = False
    accepts_retirees: bool = False
    accepts_smokers: bool = False
    accepts_students: bool = False
    extra_keywords: list[str] | None = None

    def get_url_prefix(self) -> str:
        accomodation_type: str = "+".join(self.accomodation_type)
        url: str = f"/{accomodation_type}/"
        if self.location is not None:
            url += self.location + "/"

        options: str = ""
        if self.min_amount:
            options += f"min-{self.min_amount}+"
        if self.max_amount:
            options += f"min-{self.max_amount}+"
        if self.bills_included:
            options += "bills-included+"
        if self.women_household:
            options += "all-female+"
        if self.length_of_stay:
            options += f"{self.length_of_stay.value}+"
        if self.available_from:
            date: str = datetime.datetime.strftime(self.available_from, "%d-%m-%Y")
            options += f"available-{date}+"
        if self.room_type:
            options += f"{self.room_type.value}+"
        if self.furnishings:
            options += f"{self.furnishings.value}+"
        if self.bathroom_options:
            options += f"{self.bathroom_options.value}+"
        if self.num_bedrooms:
            options += f"{self.num_bedrooms.value}+"
        if self.parking:
            options += f"{self.parking.value}+"
        if self.backpackers:
            options += "backpackers+"
        if self.children:
            options += "children+"
        if self.lgbt:
            options += "lgbt-friendly+"
        if self.over:
            options += "over-40+"
        if self.pets:
            options += "pets+"
        if self.retirees:
            options += "retirees+"
        if self.smokers:
            options += "smokers+"
        if self.students:
            options += "students+"
        if self.keywords:
            options += f"keywords-{'-'.join(self.keywords)}+"

        return (url + options).rstrip("+/") + "?page={page}"


FlatmatesRoomFilter(
    location="sydney",
    women_household=True,
    bills_included=True,
    length_of_stay="6-weeks",
    available_from=datetime.date(2024, 1, 11),
    pets=True,
    keywords=["a", "b"],
).to_url()
