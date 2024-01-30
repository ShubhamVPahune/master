import java.io.*;
import java.util.*;

interface IAnimal {
    void setId(int id);
    int getId();
    void setSpecies(String species);
    String getSpecies();
    void setName(String name);
    String getName();
    void setAge(int age);
    int getAge();
}

interface IZoo {
    void addAnimal(IAnimal animal);
    void removeAnimal(int id);
    int countAnimals();
    List<IAnimal> getAnimalsBySpecies(String species);
    Map<Integer, List<IAnimal>> getAnimalsByAge();
}

class Animal implements IAnimal {
    private int id;
    private int age;
    private String species;
    private String name;

    @Override
    public void setId(int id) {
        this.id = id;
    }

    @Override
    public int getId() {
        return this.id;
    }

    @Override
    public void setSpecies(String species) {
        this.species = species;
    }

    @Override
    public String getSpecies() {
        return this.species;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public int getAge() {
        return this.age;
    }
}

class Zoo implements IZoo {
    private Map<Integer, IAnimal> animals = new HashMap<>();

    @Override
    public void addAnimal(IAnimal animal) {
        animals.put(animal.getId(), animal);
    }

    @Override
    public void removeAnimal(int id) {
        animals.remove(id);
    }

    @Override
    public int countAnimals() {
        return animals.size();
    }

    @Override
    public List<IAnimal> getAnimalsBySpecies(String species) {
        List<IAnimal> animalsBySpecies = new ArrayList<>();
        for (IAnimal animal : animals.values()) {
            if (animal.getSpecies().equals(species)) {
                animalsBySpecies.add(animal);
            }
        }
        return animalsBySpecies;
    }

    @Override
    public Map<Integer, List<IAnimal>> getAnimalsByAge() {
        Map<Integer, List<IAnimal>> animalsByAge = new HashMap<>();
        for (IAnimal animal : animals.values()) {
            int age = animal.getAge();
            animalsByAge.computeIfAbsent(age, k -> new ArrayList<>()).add(animal);
        }
        return animalsByAge;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        // Your main method remains unchanged
    }
}
