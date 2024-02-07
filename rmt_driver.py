from objects.Model import Model
from objects.RMT_UI import RMT_UI
from utils.rmt_utils import *

def main():
    # Initialize hardware
    # Instantiate UI object
    rmt_model = Model(10, 10)
    ui_object = RMT_UI(rmt_model)
    
    while (True):
        ui_input = ui_object.getInput()
        if ui_input == INCREASE_SPEED:
            rmt_model.increase_speed()
        if ui_input == DECREASE_SPEED:
            rmt_model.decrease_speed()
        if ui_input == INCREASE_SPIN:
            rmt_model.increase_spin()
        if ui_input == DECREASE_SPIN:
            rmt_model.decrease_spin()
        if ui_input == INCREMENT_MODE:
            rmt_model.increment_mode()
        if ui_input == DECREMENT_MODE:
            rmt_model.decrement_mode()
        if ui_input != None:
            print(f"ui input: {ui_input}")
            ui_object.updateView(rmt_model)


if __name__ == "__main__":
    main()
