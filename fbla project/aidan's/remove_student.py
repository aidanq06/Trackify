import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random as rand
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
import pyglet

def remove_student(listbox):
    print(listbox.selection())