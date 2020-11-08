using System;
using System.Dynamic;

namespace ConsoleAppDynamicObject {
    public class MonObjet: DynamicObject {
        public override bool TryGetMember(
                GetMemberBinder binder, out object result) {
            result = binder.Name;
            return true;
        }
    }
    class Program {
        static void Main(string[] args) {
            dynamic obj = new MonObjet();
            Console.WriteLine(obj.SampleProperty);
        }
    }
}
