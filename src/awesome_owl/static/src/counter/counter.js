/** @odoo-module */

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class Counter extends Component {
    static template = "awesome_owl.Counter";
    static props = {
        onChange: { type: Function, optional: true }
    };

    setup() {
        this.state = useState({ value: 1 });
        this.orm = useService("orm");
    }

    async increment() {
        this.state.value = this.state.value + 1;
        const var1 = await this.orm.search("ir.model", [], { limit: 1 });

        console.log(var1);
        const var2 = await this.orm.call("ir.model", "search", [[1]], { limit: 1 });

        if (this.props.onChange) {
            this.props.onChange();
        }
    }
}
