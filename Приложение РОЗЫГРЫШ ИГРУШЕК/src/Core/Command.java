package Core;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Command {
    Scanner input = new Scanner(System.in);
    ArrayList<Toy> array = new ArrayList<>();

    public void add(){
        System.out.println("Название игрушки: ");
        String name = input.next();
        System.out.println("Кол-во игрушки: ");
        int count = input.nextInt();
        Toy toy = new Toy(name, count);

        System.out.println("Сохранить? 1 - ДА, 2 - НЕТ");
        int bool = input.nextInt();
        if (bool == 1){
            array.add(toy);
        } else if (bool == 2) {
            System.out.println("Отменено");
        } else {
            System.out.println("неправильный ввод");
        }
        
    }

    public void randomDrop(){
        int sum = 0;

        for (Toy toy : array) {
            sum += toy.count;
        }

        Random x = new Random();
        int mass = x.nextInt(sum);

        for (Toy toy : array) {
            mass -= toy.count;
            if (mass <= 0){
                System.out.printf("Вы получили: %s\n", toy.name);
                toy.count -= 1;
                if (toy.count == 0){
                    array.remove(toy);
                    return;
                }
            }
        }
        
    }

    public int keyIn(){
        int key = input.nextInt();
        return key;
    }

    public void read(){
        System.out.println();
        for (Toy toy : array) {
            System.out.printf("%s count: %d \n", toy.name, toy.count);
        }
    }
    

}
