from pyautocad import Autocad, APoint
import time
import comtypes
import os

def connect_to_autocad(retries=5, delay=5):
    acad = None
    for attempt in range(retries):
        try:
            acad = Autocad(create_if_not_exists=True)
            print("Connected to AutoCAD")
            return acad
        except comtypes.COMError as e:
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Failed to connect to AutoCAD after several attempts")

def draw_line_and_save():
    # Connect to AutoCAD with retries
    acad = connect_to_autocad()
    
    # Create a new drawing
    acad.app.Documents.Add()
    print("New drawing created")

    # Define start and end points for the line
    start_point = APoint(0, 0)
    end_point = APoint(10, 0)  # 10 meters (AutoCAD units)

    # Add a line to the model space
    line = acad.model.AddLine(start_point, end_point)
    acad.prompt("A 10-meter line has been drawn\n")
    print("A 10-meter line has been drawn from (0,0) to (10,0)")

    # Save the drawing to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "new_drawing.dwg")
    acad.ActiveDocument.SaveAs(file_path)
    print(f"Drawing saved as '{file_path}'")

if __name__ == "__main__":
    draw_line_and_save()
