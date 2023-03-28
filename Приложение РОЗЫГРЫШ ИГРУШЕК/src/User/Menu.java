package User;

import Core.Command;

public class Menu {
    Command c = new Command();

    public void start(){
        int key = 10;
        while (key != 0) {
            try{
            System.out.println("Введи команду: ");
            key = c.keyIn();
            if (key == 1){
                c.add();
            } else if (key == 2){
                c.randomDrop();
            } else if (key == 9){
                System.out.println("Команды:\n{1} - добавить игрушку(и)\n{2} - рандомное награждение игрушкой\n{3} - список игрушек\n{9} - список команд\n{0} - выключить приложение\n");
            } else if (key == 3){
                c.read();
            } else {
                System.out.println("неизвестная команда, {9} - список команд");
            }
        } catch(Exception command) {
            System.out.println("Исключение: не допускается ввод букв\n");
            return;
        }
        }
    }
}
