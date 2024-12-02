public class MyClass
{
    private int value;

    public MyClass SetValue(int newValue)
    {
        value = newValue;
        return this;
    }

    public MyClass Increment()
    {
        value++;
        return this;
    }
}

//usage: MyClass obj = new MyClass().SetValue(10).Increment();
